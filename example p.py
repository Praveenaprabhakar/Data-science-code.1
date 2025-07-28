import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("Admission_Predict.csv")

# Drop unnecessary columns
data = data.drop(["Research", "SOP", "LOR "], axis=1)

# Define the features and scale them
X = data.drop(["Serial No.", "GRE Score", "TOEFL Score", "University Rating", "CGPA", "Chance of Admit "], axis=1)

# Standardize the features
scaler = StandardScaler()
Xs = scaler.fit_transform(X)

# Normalize specific columns
num = ["GRE Score", "TOEFL Score", "University Rating", "CGPA", "Chance of Admit "]
scaler = MinMaxScaler()
data[num] = scaler.fit_transform(data[num])

# Perform KMeans clustering
kmean = KMeans(n_clusters=4, random_state=42)
data["cluster"] = kmean.fit_predict(Xs)

# Drop the columns you want to exclude from the features
X_features = data.drop(["Serial No.", "GRE Score", "TOEFL Score", "University Rating", "CGPA", "Chance of Admit ", "cluster"], axis=1)
y = data["cluster"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_features, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: ", accuracy)

# Plotting the results
plt.figure(figsize=(10, 5))
plt.scatter(y_test, y_pred, color='red', edgecolors='k', alpha=0.7)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'b--', lw=2)  
plt.xlabel('True Clusters')
plt.ylabel('Predicted Clusters')
plt.title('Cluster Prediction Scatter Plot')
plt.show()
