import matplotlib.pyplot as plt
import pandas as pd

d = pd.read_csv("college_admission.csv")

x = input("Do you want to check admission status? (yes/no): ")
if x == "yes":
    course = input("Enter course name: ")
    course_data = d[d['Course'] == course]

if not course_data.empty:
      for index,row in course_data.iterrows():  
        print("\nAdmission Details:")
        print(f"Course: {course}")
        print(f"Waitlisted: {row{'Admission Status'}}")
        print(f"Pending: {row{'Admission Status'}}")
        print(f"Enrolled: {row{'Admission Status'}}")

        
        statuses = ['Waitlisted', 'Pending', 'Enrolled']
        counts = [waitlisted, pending, enrolled]

       

       
        labels=["Waitlisted","Enrolled","Pending"]
        sizes = [40, 30, 20, ]
        plt.figure(figsize=(8, 5))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['gold', 'blue', 'red', 'green'])
        plt.title('Pie Chart')
        plt.show()


       
    else:
        print("Sorry, no records found for that course.")
