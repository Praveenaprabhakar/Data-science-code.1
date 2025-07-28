import pymysql as mysql
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, StandardScaler


con = mysql.connect(host="localhost", user="root", password="", database="praveena")
cursor = con.cursor()

cursor.execute("SELECT * FROM student")
res = cursor.fetchall()

columns = [desc[0] for desc in cursor.description]
df = pd.DataFrame(res, columns=columns)


df["date_of_birth"] = pd.to_datetime(df["date_of_birth"])
df["enrollment_date"] = pd.to_datetime(df["enrollment_date"])


cat = ["first_name", "last_name", "gender", "email"]
label_encode = LabelEncoder()
for c in cat:
    df[c] = label_encode.fit_transform(df[c])


df["dob_days"] = (df["date_of_birth"] - pd.Timestamp("1970-01-01")).dt.days
df["enrollment_days"] = (df["enrollment_date"] - pd.Timestamp("1970-01-01")).dt.days


num = ["student_id", "phone_number", "dob_days", "enrollment_days"]
df[num] = MinMaxScaler().fit_transform(df[num])


X = df.drop(["date_of_birth", "enrollment_date"], axis=1)


Xs = StandardScaler().fit_transform(X)


kmean = KMeans(n_clusters=2, random_state=42)
df["cluster"] = kmean.fit_predict(Xs)
print(df)


plt.figure(figsize=(8, 6))
plt.scatter(df["student_id"], df["enrollment_days"], c=df["cluster"], cmap="Set1", s=150, edgecolors="k")
plt.xlabel("Student ID (scaled)")
plt.ylabel("Enrollment Days (scaled)")
plt.title("KMeans Clustering of Students")
plt.colorbar(label="Cluster")
plt.grid(True)
plt.show()


