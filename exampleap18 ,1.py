import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis, zscore
from scipy import stats

# Read dataset
data = pd.read_csv("student_dataset.csv")

# 1. Mean Barplot
mean_value = {
    'metric': ["Math", "Physics"],
    'mean': [data["Math"].mean(), data["Physics"].mean()]
}
mean_value_df = pd.DataFrame(mean_value)

plt.figure(figsize=(8, 6))
sns.barplot(x='metric', y='mean', data=mean_value_df, palette='viridis')
plt.title("")
plt.xlabel('Metric')
plt.ylabel('Mean')
plt.show()

# 2. Skewness and Kurtosis
numdata = data.select_dtypes(include=["number"])

# Skewness
skewness = numdata.apply(skew)
print("Skewness Information:")
for col, skews in skewness.items():
    if skews > 0:
        print(f"{col} is positively skewed")
    elif skews < 0:
        print(f"{col} is negatively skewed")
    else:
        print(f"{col} is normally distributed")

# Barplot for skewness
plt.figure(figsize=(10, 6))
sns.barplot(x=skewness.index, y=skewness.values, palette="coolwarm")
plt.xticks(rotation=45)
plt.title("Skewness of Numerical Columns")
plt.xlabel("Feature")
plt.ylabel("Skewness")
plt.tight_layout()
plt.show()

# Kurtosis
print("\n--------------------------------------------------------")
kurt = numdata.apply(kurtosis)
print("Kurtosis Information:")
for col, k in kurt.items():
    if k > 0:
        print(f"{col} has heavy tails")
    elif k < 0:
        print(f"{col} has light tails")
    else:
        print(f"{col} has normal tails")

# 3. Z-Score for "Roll No"
data["zscore"] = zscore(data["Physics"])
print("\nData with Z-score:")
print(data)

# 4. Confidence Intervals and Visualization
numerical = ["Math", "Physics"]
confidence = 0.99
values = data[numerical]

for column in numerical:
    mean = np.mean(values[column])
    sem = stats.sem(values[column])
    ci = stats.t.interval(confidence, len(values[column]) - 1, loc=mean, scale=sem)
    l, u = ci

    print(f"\nColumn : {column}")
    print(f"Mean value : {mean}")
    print(f"Standard Error : {sem}")
    print(f"{int(confidence*100)}% Confidence Interval : {ci}")

    # Plotting confidence interval
    plt.figure(figsize=(8, 6))
    plt.axhline(mean, color="brown", linestyle="--", label="Mean")
    plt.fill_between([0, 1], l, u, color="lightblue", alpha=0.5,
                     label=f"{int(confidence*100)}% Confidence Interval")
    plt.xlim(0, 1)
    plt.ylim(min(values[column]) - 50, max(values[column]) + 50)
    plt.legend()
    plt.title(f"Confidence Interval for {column}")
    plt.ylabel(column)
    plt.show()

# 5. Z-score Histograms
mean = values.mean()
std = values.std()
z_scores = (values - mean) / std

print("\nMean:")
print(mean)
print("\nStandard Deviation:")
print(std)
print("\nOriginal Values:")
print(values)
print("\nZ-scores:")
print(z_scores)

# Plot Histograms
plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
sns.histplot(data=values.melt(), x="value", hue="variable", kde=True, palette="RdBu")
plt.title("Original Data Distribution")

plt.subplot(1, 2, 2)
sns.histplot(data=z_scores.melt(), x="value", hue="variable", kde=True, palette="pastel")
plt.title("Z-Score Normalized Distribution")

plt.tight_layout()
plt.show()
