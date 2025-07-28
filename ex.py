import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('student_dataset.csv')
print(data.describe())

# List of numerical columns
numerical = ["Physics", "Math", "Chemistry"]

# Calculate mean values
mean_value = data[numerical].mean()

# Print mean values
print("Mean Values:")
print(f"Physics: {mean_value['Physics']}")
print(f"Math: {mean_value['Math']}")
print(f"Chemistry: {mean_value['Chemistry']}")

# Line plot for Physics scores by Grade
plt.figure(figsize=(12, 6))
sns.lineplot(x='Grade', y='Physics', data=data, marker='o', color='b')

# Add labels and grid
plt.title("Physics Score by Grade")
plt.xlabel("Grade")
plt.ylabel("Physics Score")
plt.grid(True)

# Display the plot
plt.show()
