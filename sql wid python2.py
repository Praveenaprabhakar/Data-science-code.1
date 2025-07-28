import pymysql
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


connection = pymysql.connect(
    host="localhost",
    user="root",
    password="", 
    database="praveena"
)

try:
    with connection.cursor() as cursor:
       
        cursor.execute("SELECT * FROM student")
        result = cursor.fetchall()

        columns = [desc[0] for desc in cursor.description]

        
        df = pd.DataFrame(result, columns=columns)

       
        if 'date_of_birth' not in df.columns:
            print("❌ 'date_of_birth' column is missing in the table.")
        else:
            
            df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], errors='coerce')

          
            today = pd.to_datetime('today')
            df['age'] = (today - df['date_of_birth']).dt.days // 365

          
            print(df[['first_name', 'last_name', 'date_of_birth', 'age']])

           
            ab = df[df['age'] > 20]
            be = df[df['age'] < 25]

            
            label = ['Above 20', 'Below 20']
            counts = [len(ab), len(be)]

            plt.bar(label, counts, color=['green', 'black'])
            plt.title("Student Age Distribution")
            plt.ylabel("Number of Students")
            plt.show()


finally:
    connection.close()
  

