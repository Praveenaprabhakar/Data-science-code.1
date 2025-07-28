import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score


df=pd.read_csv("student_supervised_dataset.csv")

df_encode=df.copy()
df_encode=df.copy()
le=LabelEncoder()
df_encode["name"]=le.fit_transform(df_encode["name"])
df_encode["coverletter.rating"]=le.fit_transform(df_encode["coverletter.rating"])


X=df_encode.drop(["name","coverletter.rating"],axis=1)
y=df_encode["coverletter.rating"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=GaussianNB()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)
print(accuracy)


