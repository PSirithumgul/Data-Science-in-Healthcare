import pandas as pd

# Load the dataset
file_path = "HeartDisease.csv"
data = pd.read_csv(file_path)

# Detect records with NULLs or blanks in 'ca' and 'thal'
null_records = data[data[['ca', 'thal']].isnull().any(axis=1)]

# Output the records containing NULLs or blanks
print("Records containing NULLs or blanks in 'ca' or 'thal':")
print(null_records)

# Drop records with NULLs or blanks in 'ca' and 'thal'
cleaned_data = data.dropna(subset=['ca', 'thal'])

# Save the cleaned dataset to a new file
output_file = "HeartDisease_preprocessed1.csv"
cleaned_data.to_csv(output_file, index=False)

print(f"Cleaned dataset saved to {output_file}")
