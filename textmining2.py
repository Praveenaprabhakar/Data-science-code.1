import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = pd.read_csv("Clothing reviews.csv")


data = data.dropna(subset=["Review Text"]) 


tf = TfidfVectorizer(stop_words='english')
x = tf.fit_transform(data["Review Text"])
print(x)

kmean = KMeans(n_clusters=2, random_state=42)
data["Cluster"] = kmean.fit_predict(x)

cluster = data["Cluster"].value_counts().sort_index()


plt.bar(cluster.index, cluster.values, color=["green", "blue"])
plt.xticks([0, 1])
plt.xlabel("Cluster")
plt.ylabel("Number of Reviews")
plt.title("KMeans Clustering of Clothing Reviews")
plt.show()
