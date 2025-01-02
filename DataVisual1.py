import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'HeartDisease_preprocessed6.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print("First 5 rows of the dataset:")
print(data.head())

# Display the column names
print("\nColumns in the dataset:")
print(data.columns.tolist())

# Generate distplots
columns_to_plot = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
plot_titles = {
    'age': 'Distribution of Age',
    'trestbps': 'Distribution of Resting Blood Pressure',
    'chol': 'Distribution of Serum Cholesterol',
    'thalach': 'Distribution of Maximum Heart Rate Achieved',
    'oldpeak': 'Distribution of ST Depression'
}

# Create distplots for each specified column
for column in columns_to_plot:
    sns.histplot(data[column], kde=True, bins=20)
    plt.title(plot_titles[column])
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()
