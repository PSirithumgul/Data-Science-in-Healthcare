import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
file_path = "HeartDisease_preprocessed4.csv"
data = pd.read_csv(file_path)

# Boxplot for the 'chol' column
plt.figure(figsize=(8, 6))
data['chol'].plot(kind='box', vert=False)
plt.title('Boxplot of Serum Cholesterol Levels (chol)')
plt.show()

# Calculate Z-scores for the 'chol' column
mean_chol = data['chol'].mean()
std_chol = data['chol'].std()
data['z_score_chol'] = (data['chol'] - mean_chol) / std_chol

# Identify outliers using Z-score (threshold: |z| > 3)
z_outliers = data[abs(data['z_score_chol']) > 3]

# Calculate the Interquartile Range (IQR) for the 'chol' column
Q1 = data['chol'].quantile(0.25)
Q3 = data['chol'].quantile(0.75)
IQR = Q3 - Q1

# Identify outliers using IQR (threshold: outside [Q1 - 1.5*IQR, Q3 + 1.5*IQR])
iqr_outliers = data[(data['chol'] < Q1 - 1.5 * IQR) | (data['chol'] > Q3 + 1.5 * IQR)]

# Combine Z-score and IQR outliers (union of both methods)
outliers = pd.concat([z_outliers, iqr_outliers]).drop_duplicates()

# Output the outliers
print("Outliers identified in the 'chol' column:")
print(outliers[['chol', 'z_score_chol']])

# Remove outliers from the dataset
cleaned_data = data.drop(outliers.index)
cleaned_data = cleaned_data.drop(columns=['z_score_chol'])

# Save the dataset with outliers removed
output_file = "HeartDisease_preprocessed5.csv"
cleaned_data.to_csv(output_file, index=False)

print(f"Dataset with outliers removed saved to {output_file}")
