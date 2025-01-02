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

# Generate count plots for the specified columns
columns_to_plot = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'num']
plot_titles = {
    'sex': 'Count of Patients by Sex',
    'cp': 'Count of Chest Pain Types',
    'fbs': 'Count of Fasting Blood Sugar Levels',
    'restecg': 'Count of Resting Electrocardiographic Results',
    'exang': 'Count of Exercise-Induced Angina',
    'slope': 'Count of Slope of Peak Exercise ST Segment',
    'num': 'Count of Diagnosis Results (Heart Disease Presence)'
}

# Create count plots for each specified column
for column in columns_to_plot:
    sns.countplot(x=data[column], palette='Set2')
    plt.title(plot_titles[column])
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.show()
