import pandas as pd

# Load the dataset
df = pd.read_csv("HeartDisease_preprocessed9.csv")

# Check the unique values in the 'sex' and 'age' columns before transformation
print("Unique values in 'sex' and 'age' columns before transformation:")
print(df[['sex', 'age']].head())

# Create the 'gender_and_age' column based on the conditions
def categorize_gender_and_age(row):
    if row['sex'] == 1:  # Male
        if row['age'] < 45:
            return 1  # Male, age < 45, not at risk
        else:
            return 2  # Male, age >= 45, at risk
    elif row['sex'] == 0:  # Female
        if row['age'] < 55:
            return 3  # Female, age < 55, not at risk
        else:
            return 4  # Female, age >= 55, at risk

# Apply the categorization function to create the 'gender_and_age' column
df['gender_and_age'] = df.apply(categorize_gender_and_age, axis=1)

# Check the transformed 'gender_and_age' column
print("\nUnique values in 'gender_and_age' column after transformation:")
print(df['gender_and_age'].unique())

# Save the modified dataset to a new file
df.to_csv("HeartDisease_preprocessed10.csv", index=False)

# Display the updated dataset
print("\nUpdated dataset with 'gender_and_age' column:")
print(df.head())
