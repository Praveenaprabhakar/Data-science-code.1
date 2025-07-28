import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram,linkage,fcluster
from sklearn.preprocessing import *

data = pd.read_csv("supermarket.csv")
data = data.head(200)
cat=["Branch","City","Customer type","Gender","Product line","Date","Time","Payment"]
label_encode=LabelEncoder()
for  c in cat:
    data[c]=label_encode.fit_transform(data[c])
    print(data[c])

X=data.drop(["Invoice ID","Date","Time","Branch","Product line"],axis=1)
scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)

linked=linkage(X_scaled,method="ward")

dendrogram(linked,orientation="top",distance_sort="descending")
plt.show()




data=pd.read_csv("supermarket.csv")
data=data.head(100)
cat=["Invoice ID","Branch","City","Customer type","Gender","Product line","Date","Time","Payment"]
label_encode=LabelEncoder()
for  c in cat:
    data[c]=label_encode.fit_transform(data[c])
    print(data[c])

X=data.drop(["Unit price","gross margin percentage","Rating","Quantity","Tax 5%","Total","gross income","cogs"],axis=1)
scaler=StandardScaler()
k.
mean=KMeans(n_clusters=2,random_state=42)
data["cluster"]=kmean.fit_predict(X)
print(data)

plt.scatter(data["City"],data["Total"],c=data["cluster"],cmap="Set1",s=200,edgecolors="k")
plt.colorbar(label="Cluster")
plt.show()
