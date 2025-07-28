import matplotlib.pyplot as plt
import pandas as pd
import random

d = pd.read_csv("college_admission.csv")

gender_list = d['Gender'].tolist()
course_list = d['Course'].tolist()
admissionstatus_list = d['Admission Status'].tolist()

def random_gender():
    return random.choice(gender_list)

def random_course():
    return random.choice(course_list)

def random_admissionstatus():
    return random.choice(admissionstatus_list)

def sim():
    n = 1000
    gender = {"Male": 0, "Female": 0}
    course = {c: 0 for c in set(course_list)}
    admissionstatus = {"Waitlisted": 0, "Enrolled": 0, "Pending": 0}
    
    course_admission_status = {
        c: {"Waitlisted": 0, "Enrolled": 0, "Pending": 0}
        for c in set(course_list)
    }

    for i in range(n):
        g = random_gender()
        c = random_course()
        a = random_admissionstatus()
        
        gender[g] += 1
        course[c] += 1
        admissionstatus[a] += 1
        course_admission_status[c][a] += 1

    print("GENDER")
    print("Male:", gender["Male"])
    print("Female:", gender["Female"])
    print("--------------------")

    print("COURSE")
    print("Mathematics:", course["Mathematics"])
    print("Physics:", course["Physics"])
    print("Law:", course["Law"])
    print("Computer Science:", course["Computer Science"])
    print("Psychology:", course["Psychology"])
    print("Business:", course["Business"])
    print("Art:", course["Art"])
    print("Nursing:", course["Nursing"])
    print("Biology:", course["Biology"])
    print("Engineering:", course["Engineering"])
    print("--------------------------------")

    print("ADMISSIONSTATUS")
    print("Waitlisted:", admissionstatus["Waitlisted"])
    print("Enrolled:", admissionstatus["Enrolled"])
    print("Pending:", admissionstatus["Pending"])
    print("--------------------------------")

    print("COURSE ADMISSION STATUS")
    for c in sorted(course_admission_status):
        stats = course_admission_status[c]
        print(f"{c}: Waitlisted={stats['Waitlisted']}, Enrolled={stats['Enrolled']}, Pending={stats['Pending']}")
    print("--------------------")

    labels=["Waitlisted","Enrolled","Pending"]
    sizes = [40, 30, 20, ]
    plt.figure(figsize=(8, 5))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['gold', 'blue', 'red', 'green'])
    plt.title('Pie Chart')
    plt.show()

sim()
