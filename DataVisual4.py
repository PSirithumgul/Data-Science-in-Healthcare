# Importing necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
dataset_path = 'HeartDisease_preprocessed12.csv'
df = pd.read_csv(dataset_path)

# Columns to create count plots for
columns_to_plot = ['trestbps', 'chol', 'thalach', 'genage', 'slopeak']

# Set up the plotting area
plt.figure(figsize=(15, 10))

# Generate count plots
for i, column in enumerate(columns_to_plot, 1):
    plt.subplot(3, 2, i)  # Arrange plots in a grid
    sns.countplot(data=df, x=column, palette='viridis')
    plt.title(f'Count Plot of {column}')
    plt.xlabel(column)
    plt.ylabel('Count')

# Adjust layout
plt.tight_layout()
plt.show()
