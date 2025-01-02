import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'HeartDisease_preprocessed6.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print("First 5 rows of the dataset:")
print(data.head())

# Create a grouped CountPlot
plt.figure(figsize=(8, 6))
sns.countplot(data=data, x='sex', hue='num', palette='Set2')
plt.title('Count of Males and Females with and without Heart Disease')
plt.xlabel('Sex (0 = Female, 1 = Male)')
plt.ylabel('Count')
plt.legend(title='Heart Disease (num)', labels=['No (0)', 'Yes (1)'])
plt.show()
