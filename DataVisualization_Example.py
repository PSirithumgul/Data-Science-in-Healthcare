import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Dataset
data = {
    'age': [45, 54, 63, 37, 50, 41, 59, 70, 38, 48],
    'gender': [0, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    'heart_disease': [1, 0, 1, 0, 1, 1, 1, 0, 0, 1]
}

df = pd.DataFrame(data)

# DistPlot for age distribution
sns.histplot(df['age'], kde=True, bins=10, color='blue')
plt.title('Distribution of Patients by Age')
plt.xlabel('Age')
plt.ylabel('Number of Patients')
plt.show()

# CountPlot for gender distribution
sns.countplot(data=df, x='gender', palette='pastel')
plt.title('Count of Patients by Gender')
plt.xlabel('Gender (0: Female, 1: Male)')
plt.ylabel('Count')
plt.show()

# CountPlot for gender distribution by heart disease status
sns.countplot(data=df, x='gender', hue='heart_disease', palette='Set2')
plt.title('Count of Patients by Gender and Heart Disease Status')
plt.xlabel('Gender (0: Female, 1: Male)')
plt.ylabel('Count')
plt.legend(title='Heart Disease', labels=['No (0)', 'Yes (1)'])
plt.show()
