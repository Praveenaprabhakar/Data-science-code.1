import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('student_dataset.csv')
print(data.describe())

# List of numerical columns
numerical = ["Physics", "Math", "Chemistry"]

# Calculate mean values for each subject
mean_value = data[numerical].mean()

# Print mean values for each subject
print("Mean Values:")
print(f"Physics: {mean_value['Physics']}")
print(f"Math: {mean_value['Math']}")
print(f"Chemistry: {mean_value['Chemistry']}")

# Line plot for Physics, Math, and Chemistry
plt.figure(figsize=(12, 6))

# Plotting each subject
sns.lineplot(data=data, x=data.index, y='Physics', label='Physics', marker='o')
sns.lineplot(data=data, x=data.index, y='Math', label='Math', marker='s')
sns.lineplot(data=data, x=data.index, y='Chemistry', label='Chemistry', marker='^')

# Adding labels and title
plt.title('Line Chart of Physics, Math, and Chemistry Scores')
plt.xlabel('Student Index')
plt.ylabel('Scores')
plt.legend()

# Display the plot
plt.show()
