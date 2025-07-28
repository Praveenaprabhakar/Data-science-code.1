import pandas as pd
from scipy.stats import skew
import matplotlib.pyplot as plt
import seaborn as sns
fig,axes=plt.subplots(2, 2)

data=pd.read_csv("StudentsPerformance.csv")
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

sns.barplot(x=skewness.index,y=skewness.values,palette="coolwarm",ax=axes[0, 0])
axes[0, 0].set_tittle('StudentsPerformance skewness')



data=pd.read_csv("student_marks .csv")

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

sns.barplot(x=skewness.index,y=skewness.values,palette="coolwarm",ax=axes[0, 1])

axes[0, 1].set_tittle('student_marks skewness')



data=pd.read_csv("employees.csv")

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

sns.barplot(x=skewness.index,y=skewness.values,palette="coolwarm",ax=axes[1, 0])
axes[1, 0].set_tittle('employees skewness')




data=pd.read_csv("College.csv")

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

sns.barplot(x=skewness.index,y=skewness.values,palette="coolwarm",ax=axes[1, 1])
axes[1, 1].set_tittle( 'College skewness')
plt.show()
