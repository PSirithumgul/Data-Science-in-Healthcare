import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load the dataset
df = pd.read_csv("HeartDisease_preprocessed5.csv")

# Create a boxplot to visualize potential outliers in the "thalach" column
plt.figure(figsize=(8, 6))
sns.boxplot(x=df['thalach'])
plt.title('Boxplot for thalach (Heart Rate)')
plt.show()

# Z-score analysis to identify outliers
z_scores = np.abs(stats.zscore(df['thalach']))
outliers_zscore = df[z_scores > 3]  # Consider Z-score > 3 as outliers
print("Outliers based on Z-score analysis:")
print(outliers_zscore)

# Calculate IQR to identify outliers
Q1 = df['thalach'].quantile(0.25)
Q3 = df['thalach'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter the data by removing outliers based on IQR
df_no_outliers = df[(df['thalach'] >= lower_bound) & (df['thalach'] <= upper_bound)]

# Save the dataset without outliers
df_no_outliers.to_csv("HeartDisease_preprocessed6.csv", index=False)

# Display the dataset with outliers removed
print("\nDataset with outliers removed:")
print(df_no_outliers)
