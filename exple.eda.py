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

