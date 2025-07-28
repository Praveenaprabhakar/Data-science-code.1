import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

data=pd.read_csv("Pumpkin_Seeds.csv")

data = data[["Area", "Perimeter", "Major_Axis_Length", "Minor_Axis_Length", 
             "Convex_Area", "Equiv_Diameter", "Eccentricity", "Solidity", 
             "Extent", "Roundness", "Aspect_Ration"]]


mean = data.mean()
sem = data.sem() 

confidence=0.95

ci=stats.t.interval(confidence,len(data)-1,loc=mean,scale=sem)

l,u=ci

print("Mean value ",mean)
print("Standard Error ",sem)
print(ci)

plt.axhline(mean, color="pink", linestyle="--", label="Mean")
plt.fill_between([0, 1], l, u, color="red", alpha=0.5, label="95% confidence interval")
plt.xlim(0, 1)
plt.ylim(min(data)-50,max(data)+50)
plt.legend()
plt.title("Confidence Interval for ")
plt.show()
