import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read the CSV file
df = pd.read_csv('student.csv')
df.to_csv('student.csv', index=False)

# Print the DataFrame to verify the contents
print("\nRead CSV:")
print(df)

# Line plot: Math grade vs English grade
plt.figure(figsize=(8, 5))
plt.plot(df['english_grade'], df['math_grade'], label='Math Grade vs English Grade', color='b', linestyle='-', linewidth=2)
plt.xlabel('English Grade')
plt.ylabel('Math Grade')
plt.title('Line Plot: Math Grade vs English Grade')
plt.legend()
plt.grid(True)
plt.show()

# Scatter plot: Math grade vs English grade
plt.figure(figsize=(8, 5))
plt.scatter(df['math_grade'], df['english_grade'], color='r', marker='o', label='Data Points')
plt.xlabel('Math Grade')
plt.ylabel('English Grade')
plt.title('Scatter Plot: Math Grade vs English Grade')
plt.legend()
plt.grid(True)
plt.show()

# Bar plot: Average scores by subject
avg_scores = [df['math_grade'].mean(), df['english_grade'].mean(), df['science_grade'].mean()]
categories = ['Math', 'English', 'Science']
plt.figure(figsize=(8, 5))
plt.bar(categories, avg_scores, color=['blue', 'green', 'red'])
plt.xlabel('Subjects')
plt.ylabel('Average Scores')
plt.title('Average Scores by Subject')
plt.show()

# Horizontal bar plot: Average scores by subject
plt.figure(figsize=(8, 5))
plt.barh(categories, avg_scores, color=['blue', 'green', 'red'])
plt.xlabel('Average Scores')
plt.ylabel('Subjects')
plt.title('Average Scores by Subject (Horizontal)')
plt.show()

# Histogram: Age distribution
plt.figure(figsize=(8, 5))
plt.hist(df['Age'], bins=10, color='c', edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution Histogram')
plt.show()

# Pie chart: Distribution of students by subject
subject_counts = [df['math_grade'].count(), df['english_grade'].count(), df['science_grade'].count()]
labels = ['Math', 'English', 'Science']
plt.figure(figsize=(8, 5))
plt.pie(subject_counts, labels=labels, autopct='%1.1f%%', colors=['gold', 'blue', 'red'])
plt.title('Distribution of Students by Subject')
plt.show()

# Box plot: Grades by subject
data_box = [df['math_grade'], df['english_grade'], df['science_grade']]
plt.figure(figsize=(8, 5))
plt.boxplot(data_box, patch_artist=True, labels=['Math', 'English', 'Science'])
plt.title('Box Plot of Grades by Subject')
plt.show()

# Violin plot: Grades by subject
plt.figure(figsize=(8, 5))
plt.violinplot(data_box)
plt.title('Violin Plot of Grades by Subject')
plt.show()

# Stem plot: Math grade vs English grade
x = df['english_grade']
y = df['math_grade']
plt.figure(figsize=(8, 5))
plt.stem(x, y, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.title('Stem Plot: Math Grade vs English Grade')
plt.show()
