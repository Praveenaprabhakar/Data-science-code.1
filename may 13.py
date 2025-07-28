import pandas as pd
import numpy as np
from scipy.stats import skew, zscore
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data = pd.read_csv("student_dataset.csv")

# Display basic statistics
print("Descriptive Statistics:\n", data.describe())

# Numerical columns
numerical = ["Math", "Physics", "Chemistry"]

# Mean and Median
mean_values = data[numerical].mean()
median_values = data[numerical].median()

print("\nMean Values:\n", mean_values)
print("\nMedian Values:\n", median_values)

# Grade distribution countplot
plt.figure(figsize=(8, 5))
sns.countplot(x="Grade", data=data, palette="magma")
plt.title("Student Grade Distribution")
plt.xlabel("Grade")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# Skewness of numerical columns
num_data = data.select_dtypes(include=["number"])
skewness = num_data.apply(skew)
print("\nSkewness of Numerical Columns:\n", skewness)

for col, skews in skewness.items():
    if skews > 0:
        print(f"{col} is positively skewed")
    elif skews < 0:
        print(f"{col} is negatively skewed")
    else:
        print(f"{col} is normally distributed")

# Add Z-score for Math
data["Math_zscore"] = zscore(data["Math"])
print("\nData with Math Z-scores:\n", data.head())

# Z-score for all selected numerical features
values = data[numerical]
mean = values.mean()
std = values.std()
z_scores = (values - mean) / std

print("\nMeans:\n", mean)
print("\nStandard Deviations:\n", std)
print("\nOriginal Scores:\n", values.head())
print("\nZ-scores:\n", z_scores.head())

# Histogram for subject scores
plt.figure(figsize=(10, 6))
sns.histplot(data=values.melt(var_name="Subject", value_name="Score"), x="Score", hue="Subject", kde=True, palette="RdBu")
plt.title("Distribution of Subject Scores")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# --- Pie Chart Based on Math Grades ---

# Define grade converter
def assign_math_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B+'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Apply grading function
data["Math_Grade"] = data["Math"].apply(assign_math_grade)

# Count grade frequencies
grade_counts = data["Math_Grade"].value_counts().sort_index()

# Pie chart for Math grades
plt.figure(figsize=(8, 5))
plt.pie(grade_counts, labels=grade_counts.index, autopct='%1.1f%%', colors=['gold', 'blue', 'red', 'pink', 'black'])
plt.title("Math Grade Distribution")
plt.axis('equal')
plt.show()
