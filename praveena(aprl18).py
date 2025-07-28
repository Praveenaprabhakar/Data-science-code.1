import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import skew,kurtosis,zscore
from scipy import stats

df= pd.read_csv('serious.csv')
print(df.describe)
mean_value = {
    'metric': ["Period", "Series_reference"],
    'mean': [df["Period"].mean(), df["Series_reference"].mean()]}

plt.figure(figsize=(8, 6))
sns.barplot(x='metric', y='mean', data=mean_value, palette='viridis')
plt.title("Mean and Metric ")
plt.xlabel('Metric')
plt.ylabel('Mean')
plt.show()
             
numdata=data.select_dtypes(include=["number"])
skewness=numdata.apply(skew)
print("skewness information")
for col,skews in skewness.items():
    if skews>0:
      print(f"{col} is a positive skewed")
    elif skews<0:
       print(f"{col} is a negative skewed")
    else:
       print(f"{col} is normally distributted")

numdata=data.select_dtypes(include=["number"])
kurt=numdata.apply(kurtosis)

for col,k in kurt.items():
    if k>3:
        print(col,"this is heavy tails")
    elif k<3:
        print(col,"this is light tails")
    else:
        print(col,"noraml tails")


avg_scores = [df['Lower_CI'].mean(), df['Upper_CI'].mean(), df['Data_value'].mean()]
categories = ['Lower_CI', 'Upper_CI', 'Data_value']
plt.figure(figsize=(8, 5))
plt.bar(categories, avg_scores, color=['blue', 'green', 'red'])
plt.xlabel('Period')
plt.ylabel('Type')
plt.title('bar chart')
plt.show()
