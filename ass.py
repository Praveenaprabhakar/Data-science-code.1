import pandas as pd
import random

# Load your existing dataset
df = pd.read_csv("large_supermarket_transactions.csv")

# List of fruits
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes", "Pineapple", "Papaya", "Guava", "Watermelon", "Pear"]

# Find the current max TransactionID
max_id = df['TransactionID'].max()

# Generate 10,000 fruit-only transactions
new_rows = []
for i in range(1, 10001):
    items = ",".join(random.sample(fruits, random.randint(1, 5)))
    new_rows.append({"TransactionID": max_id + i, "Items": items})

# Create new DataFrame and combine
df_new = pd.DataFrame(new_rows)
df_combined = pd.concat([df, df_new], ignore_index=True)

# Save the new CSV
df_combined.to_csv("large_supermarket_transactions_plus_10k_fruits.csv", index=False)
print("✅ New CSV file created: large_supermarket_transactions_plus_10k_fruits.csv")
