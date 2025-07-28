import matplotlib.pyplot as plt
import pandas as pd

# Load the CSV file
df = pd.read_csv('student.csv')

# Save the CSV without the index (this is fine but unnecessary if you're not modifying the data)
df.to_csv('student.csv', index=False)

# Print the DataFrame to verify the contents
print("\nRead CSV:")
print(df)

# Line plot: Math Score vs English Score
plt.figure(figsize=(8, 5))
plt.plot(df['English_Score'], df['Math_Score'], label='Math Score vs English Score', color='b', linestyle='-', linewidth=2)
plt.xlabel('English Score')
plt.ylabel('Math Score')
plt.title('Line Plot')
plt.legend()
plt.grid()
plt.show()

# Scatter plot: Math Score vs English Score
plt.figure(figsize=(8, 5))
plt.scatter(df['Math_Score'], df['English_Score'], color='r', marker='o', label='Data Points')
plt.xlabel('Math Score')
plt.ylabel('English Score')
plt.title('Scatter Plot')
plt.legend()
plt.grid()
plt.show()

# Bar chart for average scores across subjects
avg_scores = [df['Math_Score'].mean(), df['English_Score'].mean(), df['Science_Score'].mean()]
categories = ['Math', 'English', 'Science']
plt.figure(figsize=(8, 5))
plt.bar(categories, avg_scores, color=['blue', 'green', 'red'])
plt.xlabel('Subjects')
plt.ylabel('Average Scores')
plt.title('Bar Chart')
plt.show()

# Horizontal Bar chart for average scores across subjects
plt.figure(figsize=(8, 5))
plt.barh(categories, avg_scores, color=['blue', 'green', 'red'])
plt.xlabel('Average Scores')
plt.ylabel('Subjects')
plt.title('Average Scores in Subjects (Horizontal)')
plt.show()

# Histogram for Age distribution
plt.figure(figsize=(8, 5))
plt.hist(df['Age'], bins=10, color='c', edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution Histogram')
plt.show()

# Pie chart for subject counts
subject_counts = [df['Math_Score'].count(), df['English_Score'].count(), df['Science_Score'].count()]
labels = ['Math', 'English', 'Science']
plt.figure(figsize=(8, 5))
plt.pie(subject_counts, labels=labels, autopct='%1.1f%%', colors=['gold', 'blue', 'red'])
plt.title('Subject Distribution Pie Chart')
plt.show()

# Boxplot for Math, English, and Science Scores
data_box = [df['Math_Score'], df['English_Score'], df['Science_Score']]
plt.figure(figsize=(8, 5))
plt.boxplot(data_box, patch_artist=True, labels=['Math', 'English', 'Science'])
plt.title('Box Plot')
plt.show()

# Violin plot for Math, English, and Science Scores
plt.figure(figsize=(8, 5))
plt.violinplot(data_box)
plt.title('Violin Plot')
plt.show()

# Stem plot: English Score vs Math Score
x = df['English_Score']
y = df['Math_Score']
plt.figure(figsize=(8, 5))
plt.stem(x, y, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.title('Stem Plot')
plt.show()
