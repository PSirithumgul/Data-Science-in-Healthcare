import pandas as pd

# Load the dataset
df = pd.read_csv("HeartDisease_preprocessed8.csv")

# Check the unique integers in the 'thalach' column before transformation
print("Unique values in 'thalach' column before transformation:")
print(df['thalach'].unique())

# Convert the 'thalach' column to categorical data based on the calculation using 'age'
def categorize_heart_rate(row):
    # Calculate (220 - age) * 0.85
    max_heart_rate = (220 - row['age']) * 0.85
    if max_heart_rate >= row['thalach']:
        return 0  # Not at risk of heart disease
    else:
        return 1  # At risk of heart disease

# Apply the categorization function to the 'thalach' column
df['thalach'] = df.apply(categorize_heart_rate, axis=1)

# Check the transformed 'thalach' column
print("\nUnique values in 'thalach' column after transformation:")
print(df['thalach'].unique())

# Save the modified dataset to a new file
df.to_csv("HeartDisease_preprocessed9.csv", index=False)

# Display the updated dataset
print("\nUpdated dataset with transformed 'thalach' column:")
print(df.head())
