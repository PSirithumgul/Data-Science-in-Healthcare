from ucimlrepo import fetch_ucirepo
import pandas as pd

# Fetch dataset
heart_disease = fetch_ucirepo(id=45)

# Extract features and targets as pandas DataFrames
X = heart_disease.data.features
y = heart_disease.data.targets

# Combine features and targets into a single DataFrame
heart_disease_df = pd.concat([X, y], axis=1)

# Save to a CSV file
csv_filename = "HeartDisease.csv"
heart_disease_df.to_csv(csv_filename, index=False)

print(f"Dataset saved as {csv_filename}")

# Metadata
print("Metadata:")
print(heart_disease.metadata)

# Variable information
print("\nVariable Information:")
print(heart_disease.variables)
