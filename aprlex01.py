import pandas as pd
from scipy.stats import kurtosis
import matplotlib.pyplot as plt
import seaborn as sns

# Function to classify kurtosis for each dataset
def classify_kurtosis(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)
    
    # Select numeric columns
    numdata = data.select_dtypes(include=["number"])
    
    # Calculate kurtosis for each numeric column
    kurt = numdata.apply(kurtosis)
    
    # Print classification of each column's kurtosis value
    for col, k in kurt.items():
        if k > 3:
            print(f"{col} in {file_path} has heavy tails")
        elif k < 3:
            print(f"{col} in {file_path} has light tails")
        else:
            print(f"{col} in {file_path} has normal tails")
    
    return kurt

# List of CSV files to process
file_paths = [
    "serious.csv",
    "employees.csv",
    "Pumpkin_Seeds.csv",
    "College.csv",
    "student_dataset.csv"
]

# Store kurtosis data for plotting
kurtosis_data = {}

# Process each file
for file_path in file_paths:
    kurt = classify_kurtosis(file_path)
    kurtosis_data[file_path] = kurt

# Plot kurtosis for each dataset (choose one dataset to plot for now)
# We'll plot the kurtosis of one of the datasets, for example, "serious.csv"

file_to_plot = "serious.csv"
kurt = kurtosis_data[file_to_plot]

sns.barplot(x=kurt.index, y=kurt.values, palette="coolwarm")
plt.xlabel('Columns')
plt.ylabel('Kurtosis')
plt.title(f'Kurtosis of Each Numeric Column in {file_to_plot}')
plt.show()
