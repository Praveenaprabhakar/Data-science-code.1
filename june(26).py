import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import *
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score



df=pd.read_csv("data set/Company_Data.csv")

print("\n data information")
print("DATA INFORMATION:",df.info())

columns = ["Sales", "CompPrice", "Income", "Advertising", "Population", "Price", 
           "ShelveLoc", "Age", "Education", "Urban", "US"]
for col in columns:
    print("\n Grouped by {col}")
    print(df.groupby(col).size())

cat=["ShelveLoc","Urban","US"]
label_encode=LabelEncoder()
for  c in cat:
    df[c]=label_encode.fit_transform(df[c])
    print(df[c])

num=["Sales","CompPrice","Income","Advertising","Population","Price","Age","Education"]
scaler=MinMaxScaler()
df[num]=scaler.fit_transform(df[num])
print(df[num])

df_encode=df.copy()
le=LabelEncoder()
df_encode["Urban"]=le.fit_transform(df_encode["Urban"])
df_encode["US"]=le.fit_transform(df_encode["US"])


X=df_encode.drop(["Urban","US"],axis=1)
y=df_encode["Urban"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model = GaussianNB()
model.fit(X_train, y_train)
y_pred=model.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)
print("\nAccuracy ==>",accuracy)



