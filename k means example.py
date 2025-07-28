import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import seaborn as sns


data = pd.read_csv("Country-data.csv")
X = data.drop(["country"], axis=1)


scaler = StandardScaler()
Xs = scaler.fit_transform(X)


kmean = KMeans(n_clusters=2, random_state=42)
data["cluster"] = kmean.fit_predict(Xs)
print(data)


plt.scatter(data["imports"],data["exports"],c=data["cluster"],cmap="Set1",s=200,edgecolors="k")
plt.colorbar(label="Cluster")
plt.show()


X = data[["child_mort", "exports", "health", "imports", "income", "inflation", "life_expec", "total_fer", "gdpp"]]
y = data["cluster"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred=model.predict(X_test)

accuracy=accuracy_score(y_test,y_pred)
print("accuracy:",accuracy)




plt.figure(figsize=(10, 5))
plt.scatter(y_test, y_pred, color='red', edgecolors='k', alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'b--', lw=2)  
plt.xlabel('Actual Grades')
plt.ylabel('Predicted Grades')
plt.title('scatter plot')
plt.show()
