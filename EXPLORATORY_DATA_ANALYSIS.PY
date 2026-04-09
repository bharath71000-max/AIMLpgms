import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("data.csv")

# Basic info
print(data.head())
print(data.info())
print(data.describe())

# Check missing values
print(data.isnull().sum())

# Histogram
data['Age'].hist()
plt.show()

# Scatter plot
plt.scatter(data['Age'], data['Salary'])
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()