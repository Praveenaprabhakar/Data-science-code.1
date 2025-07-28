import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv("data set/file_out.csv")

print("\nINFO:")
print(data.info())

print("\nDESCRIPTION:")
print(data.describe())

print("\nCOLUMNS:")
print(data.columns)
print(data.isnull().sum())
print(data.dropna())  




data['Date'] = pd.to_datetime(data['Date'])


daily_DocumentID=data.groupby('Date')['DocumentID'].sum()
print(daily_DocumentID)
plt.figure(figsize=(10, 4))
daily_DocumentID.plot(kind='line', marker='o')
plt.title("Daily Total Revenue")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.grid(True)
plt.tight_layout()
plt.show()

