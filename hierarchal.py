import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import *
from scipy.cluster.hierarchy import dendrogram,linkage,fcluster

data=pd.read_csv("Company_Data.csv")

cat=["ShelveLoc","Urban","US"]
label_encode=LabelEncoder()
for  c in cat:
    data[c]=label_encode.fit_transform(data[c])
    print(data[c])


X=data.drop(["Sales","CompPrice","Income","Advertising","Population","Price","Age","Education"],axis=1)


scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)

linked=linkage(X_scaled,method="ward")

dendrogram(linked,orientation="top",distance_sort="descending")
plt.show()

