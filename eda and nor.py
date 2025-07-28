import pandas as pd
import numpy as np
from scipy.stats import skew
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore
from scipy import stats

data=pd.read_csv("student_dataset.csv")
print(data.describe())

numberical=["Math","Physics","Chemistry"]

meanvalue=data[numberical].mean()
print(meanvalue)
 
medianvalue=data[numberical].median()
print(medianvalue)

sns.countplot(x="Grade",data=data,palette="magma")
plt.show()


numdata=data.select_dtypes(include=["number"])
skewness=numdata.apply(skew)
print(skewness)
for col,skews in skewness.items():
    if skews>0:
      print(f"{col} is a positive skewed")
    elif skews<0:
       print(f"{col} is a negative skewed")
    else:
       print(f"{col} is normally distributted")


sample=data["Math"]
data["zscore"]=zscore(sample)
print(data)

numberical=["Math","Physics","Chemistry"]

values = data[numberical]

mean = values.mean()
std = values.std()
z_scores = (values - mean) / std

print("MEAN:",mean)
print("STD:",std)
print("VALUES:",values)
print("Z_SCORES", z_scores)


sns.histplot(data=values.melt(), x="value", hue="variable", kde=True, palette="RdBu")
plt.show()

grade_bins = [0, 59, 69, 79, 89, 100]
grade_labels = ['F', 'D', 'C', 'B+', 'A']


def assign_grade(score):
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

data['Math_Grade'] = data['Math'].apply(assign_grade)
data['Physics_Grade'] = data['Physics'].apply(assign_grade)
data['Chemistry_Grade'] = data['Chemistry'].apply(assign_grade)

def plot_grade_pie(subject_grade, subject_name):
    grade_counts = subject_grade.value_counts().reindex(grade_labels)
    sizes = grade_counts.values
    labels = grade_counts.index
    
    plt.figure(figsize=(8, 5))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['gold', 'blue', 'red', 'pink', 'black'])
    plt.title(f'{subject_name} Grade Distribution')
    plt.axis('equal')
    plt.show()


subjects = ['Math', 'Physics', 'Chemistry']
for subject in subjects:
    plot_grade_pie(data[f'{subject}_Grade'], subject)
