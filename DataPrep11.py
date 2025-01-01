import pandas as pd

# Load the dataset
df = pd.read_csv("HeartDisease_preprocessed10.csv")

# Check the unique values in the 'slope' and 'oldpeak' columns before transformation
print("Unique values in 'slope' and 'oldpeak' columns before transformation:")
print(df[['slope', 'oldpeak']].head())

# Create the 'slope_and_oldpeak' column based on the conditions
def categorize_slope_and_oldpeak(row):
    if row['slope'] == 1:
        return 0  # Not at risk
    elif row['slope'] in [2, 3]:
        if row['oldpeak'] < 1:
            return 0  # Not at risk
        else:
            return 1  # At risk
    else:
        return None  # Handle unexpected values if any

# Apply the categorization function to create the 'slope_and_oldpeak' column
df['slope_and_oldpeak'] = df.apply(categorize_slope_and_oldpeak, axis=1)

# Check the transformed 'slope_and_oldpeak' column
print("\nUnique values in 'slope_and_oldpeak' column after transformation:")
print(df['slope_and_oldpeak'].unique())

# Save the modified dataset to a new file
df.to_csv("HeartDisease_preprocessed11.csv", index=False)

# Display the updated dataset
print("\nUpdated dataset with 'slope_and_oldpeak' column:")
print(df.head())
