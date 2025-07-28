import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram,linkage,fcluster
from sklearn.preprocessing import *

data = pd.read_csv("supermarket.csv")
data = data.head(200)
cat=["Branch","City","Customer type","Gender","Product line","Date","Time","Payment"]
label_encode=LabelEncoder()
for  c in cat:
    data[c]=label_encode.fit_transform(data[c])
    print(data[c])

data_sorted = data.sort_values(by='Unit price', ascending=False)
print("\nSorted DataFrame:")
print(data_sorted)

pivot_data = data.pivot_table(values='Product line', index='Quantity')
print("\nPivot Table:")
print(pivot_data)
    
data.rename(columns={'City': 'area'}, inplace=True)
print("\nRenamed Columns:")
print(data)

data_reset = data.reset_index()
print("\nReset Index:")
print(data_reset)

data.set_index('Customer type', inplace=True)
print("\nSet Index:")
print(data)

data_duplicate = pd.DataFrame(data.iloc[0])
print("\nDataFrame with Duplicates:")
print(data_duplicate.duplicated())
print("\nAfter Dropping Duplicates:")
print(data_duplicate.drop_duplicates())

X=data.drop(["Invoice ID","Date","Time","Branch","Product line"],axis=1)
scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)

linked=linkage(X_scaled,method="ward")

dendrogram(linked,orientation="top",distance_sort="descending")
plt.show()

