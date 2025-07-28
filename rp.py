import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random


data = pd.read_csv("StudentsPerformance.csv")


gender_counts = data['gender'].value_counts(normalize=True)
female_prob = gender_counts['female']
male_prob = gender_counts['male']


def gender():
    return np.random.choice(['female', 'male'], p=[female_prob, male_prob])

def sim():
    n = 1000
    result = {"female": 0, "male": 0}
    
    for _ in range(n):
        result[gender()] += 1print("female:", result["female"])
    print("male:  ", result["male"])

    
    female_ratio = result["female"] / n
    male_ratio = result["male"] / n

    print("Proportion female:", female_ratio)
    print("Proportion male:  ", male_ratio)


    labels = list(result.keys())
    counts = list(result.values())
    plt.bar(labels, counts, color=["red", "green"])
    plt.title("Gender Simulation Based on Dataset Distribution")
    plt.ylabel("Count")
    plt.show()


sim()
