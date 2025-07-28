import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("Pumpkin_Seeds.csv")
data = data[["Area", "Perimeter", "Major_Axis_Length", "Minor_Axis_Length", 
             "Convex_Area", "Equiv_Diameter", "Eccentricity", "Solidity", 
             "Extent", "Roundness", "Aspect_Ration"]]


mean = data.mean()
std=data.std()

z_score=(data-mean)/std

print(mean,std,data,data["z-distri"],sep="\n")


plt.subplot(1,2,1)
sns.histplot(data,kde=True,color="skyblue")
plt.subplot(1,2,2)
sns.histplot(data["z-distri"],kde=True,color="red")
plt.show() 
