import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import *


data=pd.read_csv("data set/supermarket.csv",encoding='ISO-8859-1')
data=data.drop(columns=["Invoice ID","Time","Date"])
                        
num=["Quantity","Unit price","Tax 5%","Total","Rating","cogs","gross margin percentage","gross income"]
scaler=MinMaxScaler()
data[num]=scaler.fit_transform(data[num])
print(data[num])


cat=["Branch","City","Payment","Customer type","Product line","Gender"]
label_encode=LabelEncoder()
for  c in cat:
    data[c]=label_encode.fit_transform(data[c])
    print(data[c])


data_encode=data.copy()
le=LabelEncoder()
data_encode["City"]=le.fit_transform(data_encode["City"])
data_encode["Customer type"]=le.fit_transform(data_encode["Customer type"])


X=data_encode.drop(["City","Customer type"],axis=1)
y=data_encode["Customer type"]


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model=RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(X_train,y_train)

y_pred=model.predict(X_test)

accuracy=accuracy_score(y_test,y_pred)

print("accuracy:",accuracy)


data=pd.read_csv("data set/supermarket.csv")

data=data.drop(columns=["Invoice ID","Time","Date"])


scaler=StandardScaler()
Xs=scaler.fit_transform(X)

kmean=KMeans(n_clusters=2 ,random_state=42)
data["cluster"]=kmean.fit_predict(Xs)
print(data)

plt.scatter(data["Customer type"],data["Product line"],c=data["cluster"],cmap="Set1",s=200,edgecolors="k")
plt.colorbar(label="Cluster")
plt.show()


plt.figure(figsize=(10, 5))
plt.scatter(y_test, y_pred, color='red', edgecolors='k', alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'b--', lw=2)  
plt.xlabel('Actual Grades')
plt.ylabel('Predicted Grades')
plt.title('scatter plot')
plt.show()


