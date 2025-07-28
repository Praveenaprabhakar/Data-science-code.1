import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("Pumpkin_Seeds.csv")


data = data[["Area", "Perimeter", "Major_Axis_Length", "Minor_Axis_Length", 
             "Convex_Area", "Equiv_Diameter", "Eccentricity", "Solidity", 
             "Extent", "Roundness", "Aspect_Ration"]]

mean = data.mean()
sem = data.sem()

confidence = 0.95


ci = stats.t.interval(confidence, len(data) - 1, loc=mean, scale=sem)


l, u = ci


print("Mean value:\n", mean)
print("Standard Error:\n", sem)
print("95% Confidence Interval:\n", ci)

plt.figure(figsize=(10, 6))
columns = data.columns.tolist()
for i in range(len(columns)):
    column = columns[i] 
    plt.subplot(4, 3, i + 1) 
    plt.axhline(mean[column], color="pink", linestyle="--", label="Mean")
    plt.fill_between([0, 1], l[i], u[i], color="red", alpha=0.5, label="95% Confidence Interval")
    plt.xlim(0, 1)
    plt.ylim(min(data[column]) - 50, max(data[column]) + 50)
    plt.title(column)
    plt.legend()

plt.tight_layout()
plt.show()
