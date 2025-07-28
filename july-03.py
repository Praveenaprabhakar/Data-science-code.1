import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import *
from scipy.cluster.hierarchy import dendrogram,linkage,fcluster
from sklearn.preprocessing import *
import numpy as np
import pandas as pd

random_numbers = np.random.randint(1, 6, size=2000)
print(random_numbers)

product = ['milk', 'curd', 'bread', 'butter', 'millets']
random_product = np.random.choice(product, size=2000)

branch = ['mayiladuthurai','thanjavur','thrichy','covai','kumbakonam']
random_branch= np.random.choice(branch, size=2000)
df = pd.DataFrame({

'randomnumbers': random_numbers,
    'product': random_product,
    'branch' :random_branch
})




data=pd.read_csv("random.csv")

cat=["product","branch"]
label_encode=LabelEncoder()
for  c in cat:
    data[c]=label_encode.fit_transform(data[c])
    print(data[c])



num=["randomnumbers"]
scaler=MinMaxScaler()
data[num]=scaler.fit_transform(data[num])
print(data[num])

X=data.drop(["randomnumbers"],axis=1)


scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)

linked=linkage(X_scaled,method="ward")

dendrogram(linked,orientation="top",distance_sort="descending")
plt.show()



