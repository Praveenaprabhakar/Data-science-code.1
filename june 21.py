import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


df=pd.read_csv("data set/credit_card_customer_data.csv")
X=df.drop(columns=["Sl_No"])
print(X)

xs=StandardScaler().fit_transform(X)
print(xs)

pca=PCA(n_components=2)
xp=pca.fit_transform(xs)
print(xp)

plt.scatter(xp[:,0],xp[:,1])
plt.show()

data=pd.read_csv("data set/credit_card_customer_data.csv")

X=data.drop(["Sl_No"],axis=1)

scaler=StandardScaler()
Xs=scaler.fit_transform(X)

kmean=KMeans(n_clusters=2 ,random_state=42)
data["cluster"]=kmean.fit_predict(Xs)
print(data)

plt.scatter(data["Customer Key"],data["Avg_Credit_Limit"],c=data["cluster"],cmap="Set1",s=200,edgecolors="k")
plt.colorbar(label="Cluster")
plt.show()




X=data[["Customer Key","Avg_Credit_Limit","Total_Credit_Cards","Total_visits_bank","Total_visits_online","Total_calls_made"]]
y=data["Sl_No"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model=RandomForestClassifier(random_state=42)
model.fit(X_train,y_train)

y_pred=model.predict(X_test)

accuracy=accuracy_score(y_test,y_pred)



plt.figure(figsize=(10, 5))
plt.scatter(y_test, y_pred, color='red', edgecolors='k', alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'b--', lw=2)  
plt.xlabel('Actual Grades')
plt.ylabel('Predicted Grades')
plt.title('scatter plot')
plt.show()






