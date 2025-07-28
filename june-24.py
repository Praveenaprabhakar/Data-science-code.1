import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer


df = pd.read_csv("data set/customer segemtation.csv")

cat = ["Gender", "Ever_Married", "Graduated", "Profession", "Spending_Score", "Var_1"]
label_encode = LabelEncoder()
for c in cat:
    df[c] = label_encode.fit_transform(df[c])
    print(df[c].head()) 

num = ["ID", "Age", "Family_Size", "Work_Experience"]
scaler_minmax = MinMaxScaler()
df[num] = scaler_minmax.fit_transform(df[num])
print(df[num].head())

X = df.drop(columns=["Gender"])


imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X) 


scaler_std = StandardScaler()
Xs = scaler_std.fit_transform(X_imputed)


kmean = KMeans(n_clusters=2, random_state=42)
df["cluster"] = kmean.fit_predict(Xs)  
print(df.head())


plt.scatter(df["Graduated"], df["Profession"], c=df["cluster"], cmap="Set1", s=200, edgecolors="k")
plt.colorbar(label="Cluster")
plt.show()

X_supervised = df[["ID", "Gender", "Ever_Married", "Age", "Graduated", "Profession",
                   "Work_Experience", "Spending_Score", "Family_Size", "Var_1"]]
y_supervised = df["cluster"]  


X_train, X_test, y_train, y_test = train_test_split(X_supervised, y_supervised, test_size=0.2, random_state=42)


model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)


plt.figure(figsize=(10, 5))
plt.scatter(y_test, y_pred, color='red', edgecolors='k', alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'b--', lw=2)
plt.xlabel('Actual Clusters')
plt.ylabel('Predicted Clusters')
plt.title('Actual vs Predicted Clusters')
plt.show()
