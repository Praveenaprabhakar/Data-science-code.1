import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read the CSV file and save it back without the index column
df = pd.read_csv('student.csv')
df.to_csv('student.csv', index=False)

# Print the DataFrame
print("\nRead CSV:")
print(df)

# Line plot: Math Score vs English Score
plt.figure(figsize=(8, 5))
plt.plot(df['English_score'], df['Math_Score'], label='Math Score', color='b', linestyle='-', linewidth=2)
plt.xlabel('English Score')
plt.ylabel('Math Score')
plt.title('Math Score vs English Score')
plt.legend()
plt.grid()
plt.show()

# Scatter plot: Math Score vs English Score
plt.figure(figsize=(8, 5))
plt.scatter(df['Math_Score'], df['English_score'], color='r', marker='o', label='Data Points')
plt.xlabel('Math Score')
plt.ylabel('English Score')
plt.title('Math Score vs English Score (Scatter Plot)')
plt.legend()
plt.grid()
plt.show()

# Bar chart: Average Scores by Subject
avg_scores = [df['Math_Score'].mean(), df['English_score'].mean(), df['Science_Score'].mean()]
categories = ['Math', 'English', 'Science']
plt.figure(figsize=(8, 5))
plt.bar(categories, avg_scores, color=['blue', 'green', 'red'])
plt.xlabel('Subjects')
plt.ylabel('Average Scores')
plt.title('Average Scores by Subject (Bar Chart)')
plt.show()

# Horizontal bar chart: Average Scores by Subject
plt.figure(figsize=(8, 5))
plt.barh(categories, avg_scores, color=['blue', 'green', 'red'])
plt.xlabel('Average Scores')
plt.ylabel('Subjects')
plt.title('Average Scores by Subject (Horizontal Bar Chart)')
plt.show()

# Histogram: Distribution of Age
plt.figure(figsize=(8, 5))
plt.hist(df['Age'], bins=10, color='c', edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution (Histogram)')
plt.show()

# Pie chart: Subject-wise Score Count
subject_counts = [df['Math_Score'].count(), df['English_score'].count(), df['Science_Score'].count()]
labels = ['Math', 'English', 'Science']
plt.figure(figsize=(8, 5))
plt.pie(subject_counts, labels=labels, autopct='%1.1f%%', colors=['gold', 'blue', 'red'])
plt.title('Subject-wise Score Count (Pie Chart)')
plt.show()

# Box plot: Score Distribution by Subject
data_box = [df['Math_Score'], df['English_score'], df['Science_Score']]
plt.figure(figsize=(8, 5))
plt.boxplot(data_box, patch_artist=True, labels=['Math', 'English', 'Science'])
plt.title('Score Distribution by Subject (Box Plot)')
plt.show()

# Violin plot: Score Distribution by Subject
plt.figure(figsize=(8, 5))
plt.violinplot(data_box)
plt.title('Score Distribution by Subject (Violin Plot)')
plt.show()

# Stem plot: English Score vs Math Score
x = df['English_score']
y = df['Math_Score']
plt.figure(figsize=(8, 5))
plt.stem(x, y, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.title('English Score vs Math Score (Stem Plot)')
plt.show()

