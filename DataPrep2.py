import pandas as pd

# Load the dataset
file_path = "HeartDisease_preprocessed1.csv"
data = pd.read_csv(file_path)

# Detect and correct erroneous values in the 'num' column
# Valid values: 0 or 1; convert other values (2, 3, 4) to 1
data['num'] = data['num'].apply(lambda x: 1 if x not in [0, 1] else x)

# Save the corrected dataset to a new file
output_file = "HeartDisease_preprocessed2.csv"
data.to_csv(output_file, index=False)

print(f"Corrected dataset saved to {output_file}")