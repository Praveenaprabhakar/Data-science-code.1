import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('raj.csv')




sales_trend = df.groupby('Period')['Upper_CI'].sum()


plt.figure(figsize=(10, 6)) 
plt.plot(sales_trend, marker='o', linestyle='-', color='b')
plt.title('Upper CI Trend Over Time')
plt.xlabel('Period')
plt.ylabel('Upper CI')
plt.xticks(rotation=45)  
plt.grid(True)

plt.show()
