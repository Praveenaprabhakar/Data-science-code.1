import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew,kurtosis,zscore
from scipy import stats

data = pd.read_csv("student_dataset.csv")
mean_value = {
    'metric': ["Math", "Physics","Chemistry"],
    'mean': [data["Math"].mean(), data["Physics"].mean(),data["Chemistry"].mean()]
}

plt.figure(figsize=(8, 6))
sns.barplot(x='metric', y='mean', data=mean_value, palette='magma')
plt.title("Mean and metric")
plt.xlabel('Metric')
plt.ylabel('Mean')
plt.show()

numdata = data.select_dtypes(include=["number"])
skewness = numdata.apply(skew)
print("Skewness information")

for col, skews in skewness.items():
    if skews > 0:
        print(f"{col} is positively skewed")
    elif skews < 0:
        print(f"{col} is negatively skewed")
    else:
        print(f"{col} is normally distributed")
print("--------------------------------------------------------")
kurt = numdata.apply(kurtosis)
print("Kurtosis information")
for col, k in kurt.items():
    if k > 0:
        print(f"{col} this is heavily tails")
    elif k < 0:
        print(f"{col} this is lightly tails")
    else:
        print(f"{col} normal tails")

plt.figure(figsize=(10, 6))
sns.barplot(x=skewness.index, y=skewness.values, palette="coolwarm")
plt.xticks(rotation=45)
plt.title("Skewness ")
plt.xlabel("Feature")
plt.ylabel("Skewness")
plt.tight_layout()
plt.show()

sample = data["Phone_No."]
data["zscore"] = zscore(sample)
print(data)

numerical = ["Math","Physics","Chemistry"]
values = data[numerical]
confidence = 0.99
for score in numerical:
    mean = np.mean(values[score])
    sem = stats.sem(values[score])
    ci = stats.t.interval(confidence, len(values[score]) - 1, loc=mean, scale=sem)
    l,u = ci
print("score :",score)
print("Mean:", mean)
print("sem:", sem)
print("confidence interval :", ci)
print()

plt.figure(figsize=(8, 6))
plt.axhline(mean, color="brown", linestyle="--", label="Mean")
plt.fill_between([0, 1], l, u, color="lightblue", alpha=0.5, label=f"{confidence*100}% confidence interval")
plt.xlim(0, 1)
plt.ylim(min(values[score]) - 50, max(values[score]) + 50)
plt.legend()
plt.title(score)
plt.show()

numerical = ["Math","Physics","Chemistry"]
values = data[numerical]

mean = values.mean()
std = values.std()
z_scores = (values - mean) / std
print(mean,std,values,z_scores,sep="\n")

plt.subplot(1, 2, 1)
sns.histplot(data=values.melt(), x="value", hue="variable", kde=True, palette="RdBu")
plt.subplot(1, 2, 2)
sns.histplot(data=z_scores.melt(), x="value", hue="variable", kde=True, palette="pastel")
plt.show()




