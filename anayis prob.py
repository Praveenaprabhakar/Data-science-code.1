def operation():  
 import pandas as pd
 import matplotlib.pyplot as plt


 data= pd.read_csv("adult.csv")
 
 print("select the mathamatical function:")
 print("1:age")
 print("2:workclass")
 print("3:fnlwgt")
 print("4:education") 
 print("5:education_num")
 print("6:maritalstatus")
 print("7:occupation")
 print("8:relationship")
 print("9:race")
 print("10:sex")
 print("11:capitalGain")
 print("12:capitalLoss")
 print("13:hoursPerWeek")
 print("14:nativeCountry")
 print("15:income")
 x=int(input("Enter your choice:"))

 if x ==1:
    grouped = data.groupby('age').size()
    print(grouped)
 if x ==2:
    grouped = data.groupby('workclass').size()
    print(grouped)
 if x == 3:
    grouped = data.groupby('fnlwgt"').size()
    print(grouped)
 if x ==4:
    grouped = data.groupby('education').size()
    print(grouped)
 if x ==5:
    grouped = data.groupby('education_num').size()
    print(grouped)
 if x ==6:
    grouped = data.groupby('maritalstatus').size()
    print(grouped)
 if x ==7:
    grouped = data.groupby('upation').size()
    print(grouped)
 if x ==8:
    grouped = data.groupby('relationship').size()
    print(grouped)
 if x ==9:
    grouped = data.groupby('race').size()
    print(grouped)
 if x ==10:
    grouped = data.groupby('sex').size()
    print(grouped)
 if x ==11:
    grouped = data.groupby('capitalGain').size()
    print(grouped)
 if x ==12:
    grouped = data.groupby('capitalLoss').size()
    print(grouped)                           
                           
 if x ==13:
    grouped = data.groupby('hoursPerWeek').size()
    print(grouped)
                           
 if x ==14:
    grouped = data.groupby('nativeCountry').size()
    print(grouped)
          
 if x ==15:
    grouped = data.groupby('income').size()
    print(grouped)

operation()
