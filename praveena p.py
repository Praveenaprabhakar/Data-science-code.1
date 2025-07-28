import pandas as pd
from sklearn.preprocessing import *
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

data=pd.read_csv("Admission_Predict_Ver1.1.csv")
X=data.drop(["Research","SOP","LOR "],axis=1)

scaler=StandardScaler()
Xs=scaler.fit_transform(X)


num=["Serial No.","GRE Score","TOEFL Score","University Rating","CGPA","Chance of Admit "]
scaler=MinMaxScaler()
data[num]=scaler.fit_transform(data[num])
print(data[num])

X.to_csv('Admission_Predict.csv', index=False)
data_read = pd.read_csv('Admission_Predict.csv')

kmean=KMeans(n_clusters=2,random_state=42)
data["cluster"]=kmean.fit_predict(Xs)
print(data_read)


x=data[["Serial No.","GRE Score","TOEFL Score","University Rating","CGPA","Chance of Admit "]]
y=data["cluster"]



X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(X_train,y_train)

y_pred=model.predict(X_test)

accuracy=accuracy_score(y_test,y_pred)

print("Accuracy : ",accuracy)



plt.figure(figsize=(10, 5))
plt.scatter(y_test, y_pred, color='red', edgecolors='k', alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'b--', lw=2)  
plt.xlabel('Serial No.')
plt.ylabel('CGPA')
plt.title('scatter plot')
plt.show()
