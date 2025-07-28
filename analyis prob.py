import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("employees.csv")


print(data.head())

Team=data["Team"].unique()
print(Team)

Teamvalue=data["Team"].value_counts()
print(Teamvalue)

Teamvalue.plot()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("employees.csv")

data['Start Date'] = pd.to_datetime(data['Start Date'])


daily_Salary=data.groupby('Start Date')['Salary'].sum()
print(daily_Salary)
plt.figure(figsize=(10, 4))
daily_Salary.plot(kind='line', marker='o')
plt.title("Daily Total Revenue")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.grid(True)
plt.tight_layout()
plt.show()
 
data['year'] = data['Start Date'].dt.to_period('Y')
yearly_Salary = data.groupby('year')['Salary'].sum()
print(yearly_Salary)
plt.figure(figsize=(8, 4))
yearly_Salary.plot(kind='pie',color=['teal' , 'gold', 'blue', 'red', 'green','black','skyblue','grey','orange','yellow','pink','palegreen','purple'])
plt.title('Pie Chart')
plt.show()
