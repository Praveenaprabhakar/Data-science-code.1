import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import *


df = pd.read_csv("data set/customer segemtation.csv")

cat=["Gender","Ever_Married","Graduated","Profession","Spending_Score","Var_1"]
label_encode=LabelEncoder()
for  c in cat:
    df[c]=label_encode.fit_transform(df[c])
    print(df[c])

num=["ID","Age","Work_Experience","Family_Size"]
scaler=MinMaxScaler()
df[num]=scaler.fit_transform(df[num])
print(df[num])


df_encode=df.copy()
le=LabelEncoder()
df_encode["Gender"]=le.fit_transform(df_encode["Gender"])
df_encode["Var_1"]=le.fit_transform(df_encode["Var_1"])


X=df_encode.drop(["Gender","Var_1"],axis=1)
y=df_encode["Var_1"]


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model=RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(X_train,y_train)

y_pred=model.predict(X_test)

accuracy=accuracy_score(y_test,y_pred)

print("accuracy:",accuracy)

plt.figure(figsize=(6, 4))
sns.countplot(x='Var_1', data=df_encode, palette='coolwarm')
plt.title('Countplot (Var_1)')
plt.xlabel('Var_1')
plt.ylabel('Count')
plt.tight_layout()
plt.show()
