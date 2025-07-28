import pandas as pd

d = pd.read_csv("adult.csv")

def operation():
    print("Select the mathematical function (group by column):")
    print("1: age")
    print("2: workclass")
    print("3: fnlwgt")
    print("4: education") 
    print("5: education_num")
    print("6: maritalstatus")
    print("7: occupation")
    print("8: relationship")
    print("9: race")
    print("10: sex")
    print("11: capitalGain")
    print("12: capitalLoss")
    print("13: hoursPerWeek")
    print("14: nativeCountry")
    print("15: income")
    
    x = int(input("Enter your choice (1–15): "))
    
    columns = {
        1: 'age',
        2: 'workclass',
        3: 'fnlwgt',
        4: 'education',
        5: 'education_num',
        6: 'maritalstatus',
        7: 'occupation',
        8: 'relationship',
        9: 'race',
        10: 'sex',
        11: 'capitalgain',
        12: 'capitalloss',
        13: 'hoursperweek',
        14: 'nativecountry',
        15: 'income'
    }
    
    col = columns.get(x)
    if col:
        grouped = d.groupby(col).size()
        print(f"\nGrouped count by '{col}':")
        print(grouped)
    else:
        print("Invalid choice.")

operation()
