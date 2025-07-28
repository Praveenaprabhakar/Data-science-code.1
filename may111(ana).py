import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random

d=pd.read_csv("adult.csv")
maritalstatuss_list = d['maritalstatus'].tolist()
def maritalstatus():
    return  random.choice (maritalstatuss_list)
   

def sim():
    n = 1000
    result = {"Never-married": 0, "Married-civ-spouse": 0 ,"Divorced":0, "Separated": 0, "Married-spouse-absent": 0,"Widowed": 0, "Married-AF-spouse": 0}
    
    for _ in range(n):
        result[maritalstatus()] += 1
    
    print("Never-married:" , result["Never-married"])
    print("Married-civ-spouse: ", result["Married-civ-spouse"])
    print("Divorced:",result["Divorced"])
    print("Separated:", result["Separated"])
    print("Married-spouse-absent:", result["Married-spouse-absent"])
    print("Widowed:",result["Widowed"])
    print("Married-AF-spouse:",result["Married-AF-spouse"])
    
    Nevermarried= result["Never-married"] / n
    Marriedcivspouse= result["Married-civ-spouse"] / n
    Divorced=["Divorced"] / n
    Separated=["Separated"] / n
    Marriedspouseabsent=["Married-spouse-absent"] / n
    Widowed=["Widowed"] / n
    MarriedAFspouse=["'Married-AF-spouse"] /n
    
    print("Never-married : ",Never-married)
    print("Married-civ-spouse: ", Married-civ-spouse)
    print("Divorced:", Divorced)
    print("Separated:", Separated)
    print("Married-spouse-absent:",Married-spouse-absent)
    print("Widowed:",Widowed)
    print("Married-AF-spouse:",Married-AF-spouse)
    
    labels = result.keys()
    counts = result.values()
    plt.bar(labels, counts, color=["black", "Green"])
    plt.title("bar plot")
    plt.ylabel("Count")
    plt.show()

sim()
