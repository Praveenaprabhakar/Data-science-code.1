import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv("student_dataset.csv")
print(data.describe())

sns.countplot(x="Grade",hue="Comment",data=data,palette="PRGn")
plt.show()

sns.countplot(x="Grade",hue="Physics",data=data,palette="PRGn")
plt.show()

sns.countplot(x="Grade",hue="Chemistry",data=data,palette="PRGn")
plt.show()


