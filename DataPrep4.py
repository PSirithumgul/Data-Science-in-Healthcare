import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
file_path = "HeartDisease_preprocessed3.csv"
data = pd.read_csv(file_path)

# Boxplot for the 'trestbps' column
plt.figure(figsize=(8, 6))
data['trestbps'].plot(kind='box', vert=False)
plt.title('Boxplot of Resting Blood Pressure (trestbps)')
plt.show()

# Calculate Z-scores for the 'trestbps' column
mean_trestbps = data['trestbps'].mean()
std_trestbps = data['trestbps'].std()
data['z_score_trestbps'] = (data['trestbps'] - mean_trestbps) / std_trestbps

# Identify outliers using Z-score (threshold: |z| > 3)
z_outliers = data[abs(data['z_score_trestbps']) > 3]

# Calculate the Interquartile Range (IQR) for the 'trestbps' column
Q1 = data['trestbps'].quantile(0.25)
Q3 = data['trestbps'].quantile(0.75)
IQR = Q3 - Q1

# Identify outliers using IQR (threshold: outside [Q1 - 1.5*IQR, Q3 + 1.5*IQR])
iqr_outliers = data[(data['trestbps'] < Q1 - 1.5 * IQR) | (data['trestbps'] > Q3 + 1.5 * IQR)]

# Combine Z-score and IQR outliers (union of both methods)
outliers = pd.concat([z_outliers, iqr_outliers]).drop_duplicates()

# Output the outliers
print("Outliers identified in the 'trestbps' column:")
print(outliers[['trestbps', 'z_score_trestbps']])

# Remove outliers from the dataset
cleaned_data = data.drop(outliers.index)
cleaned_data = cleaned_data.drop(columns=['z_score_trestbps'])

# Save the dataset with outliers removed
output_file = "HeartDisease_preprocessed4.csv"
cleaned_data.to_csv(output_file, index=False)

print(f"Dataset with outliers removed saved to {output_file}")
