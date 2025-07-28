import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
df = pd.read_csv('serious.csv')

# Convert 'Period' to datetime, handling errors gracefully
df['Period'] = pd.to_datetime(df['Period'], errors='coerce')  # Invalid dates become NaT

# Remove rows with invalid dates
df = df.dropna(subset=['Period'])

# Group data by 'Period' and sum the 'Units'
sales_trend = df.groupby('Period')['Units'].sum()

# Plotting the sales trend
plt.figure(figsize=(10, 6))  # Adjusted figure size for better readability
plt.plot(sales_trend, marker='o', linestyle='-', color='b')
plt.title('Daily Sales Trend')
plt.xlabel('Period')
plt.ylabel('Units')
plt.xticks(rotation=45)  # Rotate x-axis labels for clarity
plt.grid(True)

plt.show()
