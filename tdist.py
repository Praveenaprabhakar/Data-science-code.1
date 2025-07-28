import pandas as pd
import numpy as np
from scipy import stats

data = pd.read_csv("student_dataset.csv")

confidence = 0.95
n = len(data)
tdis = stats.t.ppf((1 + confidence) / 2, df=n - 1)



math = data["Math"]
mean = np.mean(math)
sem = stats.sem(math)
marginerror = tdis * sem
l = mean - marginerror
u = mean + marginerror
print("Math:")
print(mean, sem, tdis, l, u, sep="\n")
print("-"* 30)



physics = data["Physics"]
mean = np.mean(physics)
sem = stats.sem(physics)
marginerror = tdis * sem
l = mean - marginerror
u = mean + marginerror
print("Physics:")
print(mean, sem, tdis, l, u, sep="\n")
print("-" * 30)


chemistry = data["Chemistry"]
mean = np.mean(chemistry)
sem = stats.sem(chemistry)
marginerror = tdis * sem
l = mean - marginerror
u = mean + marginerror
print("Chemistry:")
print(mean, sem, tdis, l, u, sep="\n")
print("-" * 30)
