import matplotlib.pyplot as plt
import pandas as pd

d = pd.read_csv("college_admission.csv")

x = input("Do you want to check admission status? (yes/no): ")
if x.lower() == "yes":
    course = input("Enter course name: ")
    course_data = d[d['Course'] == course]

    if not course_data.empty:
    
        status_counts = course_data['Admission Status'].value_counts()

        waitlisted = status_counts.get("Waitlisted", 0)
        pending = status_counts.get("Pending", 0)
        enrolled = status_counts.get("Enrolled", 0)

        print("---Admission Details----")
        print("Course:", course)
        print("Waitlisted:", waitlisted)
        print("Pending:", pending)
        print("Enrolled:", enrolled)

       
        
        labels=["Waitlisted","Enrolled","Pending"]
        sizes = [40, 30, 20, ]
        plt.figure(figsize=(8, 5))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['pink', 'red', 'brown'])
        plt.title('Pie Chart')
        plt.show()
        
    else:
        print("Sorry, no records found for that course.")
