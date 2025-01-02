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
