import pandas as pd

# Load the dataset
df = pd.read_csv("HeartDisease_preprocessed7.csv")

# Check the unique integers in the 'trestbps' column
print("Unique values in 'trestbps' column before transformation:")
print(df['trestbps'].unique())

# Convert the 'trestbps' column to categorical data based on specified conditions
def categorize_blood_pressure(trestbps):
    if trestbps <= 129:
        return 0  # Not at risk of heart disease
    else:
        return 1  # At risk of heart disease

df['trestbps'] = df['trestbps'].apply(categorize_blood_pressure)

# Check the transformed 'trestbps' column
print("\nUnique values in 'trestbps' column after transformation:")
print(df['trestbps'].unique())

# Save the modified dataset to a new file
df.to_csv("HeartDisease_preprocessed8.csv", index=False)

# Display the updated dataset
print("\nUpdated dataset with transformed 'trestbps' column:")
print(df.head())
