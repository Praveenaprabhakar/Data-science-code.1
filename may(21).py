import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("marketing_campaign_dataset.csv")

print("Data information",data.info)
print("shape of data :",data.shape)
print("data types:",data.dtypes)
print("missing vales",data.isnull().sum())
print(".................")

grouped = data.groupby('Campaign_ID').size()
print(grouped)
plt.figure(figsize=(8,5))
plt.plot(grouped.index,grouped.values,marker='o',linestyle='-')
plt.title('Distributipn of Campaign_ID')
plt.xlabel('Campaign_ID')
plt.ylabel('count')
plt.grid(True)
plt.show()
print(".................")

grouped = data.groupby('Company').size()
print(grouped)
print("..................")

grouped = data.groupby('Campaign_Type').size()
print(grouped)
print("...................")

grouped = data.groupby('Target_Audience').size()
print(grouped)
print("..................")

grouped = data.groupby('Duration').size()
print(grouped)
print("..................")

grouped = data.groupby('Channel_Used').size()
print(grouped)
print("...................")

grouped = data.groupby('Conversion_Rate').size()
print(grouped)
print("..................")

grouped = data.groupby('Acquisition_Cost').size()
print(grouped)
print("..................")

grouped = data.groupby('ROI').size()
print(grouped)
print("...................")

grouped = data.groupby('Location').size()
print(grouped)
print("....................")

grouped = data.groupby('Language').size()
print(grouped)
print(".....................")

grouped = data.groupby('Clicks').size()
print(grouped)                           
print(".....................")

grouped = data.groupby('Impressions').size()
print(grouped)
print("......................")

grouped = data.groupby('Customer_Segment').size()
print(grouped)
print("......................")

grouped = data.groupby('Date').size()
print(grouped)

