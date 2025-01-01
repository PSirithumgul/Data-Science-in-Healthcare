import pandas as pd

# Load the dataset
df = pd.read_csv("HeartDisease_preprocessed6.csv")

# Check the unique integers in the 'chol' column
print("Unique values in 'chol' column before transformation:")
print(df['chol'].unique())

# Convert the 'chol' column to categorical data based on specified conditions
def categorize_cholesterol(chol):
    if chol < 200:
        return 1  # Desirable cholesterol level
    elif 200 <= chol < 240:
        return 2  # Borderline high cholesterol level
    else:
        return 3  # High cholesterol level

df['chol'] = df['chol'].apply(categorize_cholesterol)

# Check the transformed 'chol' column
print("\nUnique values in 'chol' column after transformation:")
print(df['chol'].unique())

# Save the modified dataset to a new file
df.to_csv("HeartDisease_preprocessed7.csv", index=False)

# Display the updated dataset
print("\nUpdated dataset with transformed 'chol' column:")
print(df.head())
