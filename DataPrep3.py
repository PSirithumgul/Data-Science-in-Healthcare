import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
file_path = "HeartDisease_preprocessed2.csv"
data = pd.read_csv(file_path)

# Boxplot for the 'age' column
plt.figure(figsize=(8, 6))
data['age'].plot(kind='box', vert=False)
plt.title('Boxplot of Age')
plt.show()

# Calculate Z-scores for the 'age' column
mean_age = data['age'].mean()
std_age = data['age'].std()
data['z_score_age'] = (data['age'] - mean_age) / std_age

# Identify outliers using Z-score (threshold: |z| > 3)
z_outliers = data[abs(data['z_score_age']) > 3]

# Calculate the Interquartile Range (IQR) for the 'age' column
Q1 = data['age'].quantile(0.25)
Q3 = data['age'].quantile(0.75)
IQR = Q3 - Q1

# Identify outliers using IQR (threshold: outside [Q1 - 1.5*IQR, Q3 + 1.5*IQR])
iqr_outliers = data[(data['age'] < Q1 - 1.5 * IQR) | (data['age'] > Q3 + 1.5 * IQR)]

# Combine Z-score and IQR outliers (union of both methods)
outliers = pd.concat([z_outliers, iqr_outliers]).drop_duplicates()

# Output the outliers
print("Outliers identified in the 'age' column:")
print(outliers[['age', 'z_score_age']])

# Remove outliers from the dataset
cleaned_data = data.drop(outliers.index)
cleaned_data = cleaned_data.drop(columns=['z_score_age'])

# Save the dataset with outliers removed
output_file = "HeartDisease_preprocessed3.csv"
cleaned_data.to_csv(output_file, index=False)

print(f"Dataset with outliers removed saved to {output_file}")