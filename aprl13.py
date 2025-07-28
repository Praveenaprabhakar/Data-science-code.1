import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

data=pd.read_csv("dataset\\supermarket.csv")

data=data["Total"]

mean=np.mean(data)
sem=stats.sem(data) 

confidence=0.95

ci=stats.t.interval(confidence,len(data)-1,loc=mean,scale=sem)

l,u=ci

print("Mean value ",mean)
print("Standard Error ",sem)
print(ci)

plt.axhline(mean,color="green",linestyle="--",label="Mean")
plt.fill_between([0,1],l,u,color="lightblue",alpha=0.5,label="95% confidence interval")
plt.xlim(0,1)
plt.ylim(min(data)-50,max(data)+50)
plt.legend()
plt.show() 
