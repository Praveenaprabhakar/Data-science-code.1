import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df= pd.read_csv('student_dataset.csv')
df.to_csv('student_dataset.csv', index=False)
print("\nRead CSV:")
print(df)

avg_scores = [df['Math'].mean(), df['Physics'].mean(), df['Chemistry'].mean()]
categories = ['Math', 'Physics', 'Chemistry']
plt.figure(figsize=(8, 5))
plt.bar(categories, avg_scores, color=['blue', 'green', 'red'])
plt.xlabel('Subjects')
plt.ylabel('Average Scores')
plt.title('Average Scores by Subject')
plt.show()

labels = ['Math','Physics', 'Chemistry']
sizes = [30, 20, 10]
plt.figure(figsize=(8, 5))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['gold', 'blue', 'red'])
plt.title('Pie Chart')
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(df['Grade'], bins=10, color='c', edgecolor='black')
plt.xlabel('Grade')
plt.ylabel(['Roll No'])
plt.title('Histogram')
plt.show()

data_box = [df['Math'], df['Physics'], df['Chemistry']]
plt.figure(figsize=(8, 5))
plt.boxplot(data_box, patch_artist=True, labels=['Math', 'Physics', 'Chemistry'])
plt.title('Box Plot')
plt.show()


plt.figure(figsize=(8, 5))
plt.violinplot(data_box)
plt.title('Violin Plot')
plt.show()

x = df['Math']
y = df['Physics']
plt.figure(figsize=(8, 5))
plt.stem(x, y, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.title('Stem Plot')
plt.show()



