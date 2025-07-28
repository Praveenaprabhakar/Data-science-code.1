import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('student_dataset.csv')
print(data.describe())

numerical=["Physics","Math","Chemistry"]

mean_value = data[numerical].mean()


print("Mean Values:")
print(f"Physics: {mean_value['Physics']}")
print(f"Math: {mean_value['Math']}")
print(f"Chemistry: {mean_value['Chemistry']}")
 
plt.figure(figsize=(10, 5))

sns.lineplot(x='Grade',y='Chemistry',data=data,marker='o',color='r')
plt.title("Grade Score by Chemistry")
plt.xlabel("Grade")
plt.ylabel("Chemistry Score")
plt.grid(True)
plt.show()


plt.figure(figsize=(12, 6))

sns.lineplot(x='Grade',y='Physics',data=data,marker='o',color='b')
plt.title("Physics Score by Grade")
plt.xlabel("Grade")
plt.ylabel("Physics Score")
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 6))

sns.lineplot(x='Grade',y='Math',data=data,marker='o',color='b')
plt.title("math Score by Grade")
plt.xlabel("Grade")
plt.ylabel("math Score")
plt.grid(True)
plt.show()

