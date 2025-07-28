import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import seaborn as sns

df=pd.read_csv("management.csv")

X=df[["parent_age","parent_salary","house_area","average_grades"]]
y=df["average_grades"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model=LinearRegression()
model.fit(X_train,y_train)

y_pred=model.predict(X_test)
print(y_test,y_pred)

print(mean_squared_error(y_test,y_pred))

import matplotlib.pyplot as plt



plt.figure(figsize=(8,5))
sns.histplot(y_pred, kde=True, color='brown')
plt.title("histogram")
plt.xlabel("Predicted Grades ")
plt.ylabel("Frequency")
plt.show()


plt.figure(figsize=(10, 5))
plt.scatter(y_test, y_pred, color='red', edgecolors='k', alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'b--', lw=2)  
plt.xlabel('Actual Grades')
plt.ylabel('Predicted Grades')
plt.title('scatter plot')
plt.show()








