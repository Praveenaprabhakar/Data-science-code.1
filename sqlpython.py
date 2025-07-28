import pymysql


connection = pymysql.connect(
host='localhost',
user='root',
password='',  # Empty password
database='praveena'


)

try:
    with connection.cursor() as cursor:
        # Drop the table if it exists
        cursor.execute("DROP TABLE IF EXISTS student")

        create_table = """
        CREATE TABLE student (
            student_id INT PRIMARY KEY,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            date_of_birth DATE,
            gender CHAR(1),
            email VARCHAR(100),
            phone_number VARCHAR(15),
            enrollment_date DATE
        );
        """
        cursor.execute(create_table)
 

        # Prepare insert query and data
        insert_query = """
        INSERT INTO student (
            student_id,
            first_name,
            last_name,
            date_of_birth,
            gender,
            email,
            phone_number,
            enrollment_date
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        data_to_insert = [
            (1, 'John', 'Doe', '2002-05-15', 'M', 'john.doe@example.com', '1234567890', '2021-08-01'),
            (2, 'Jane', 'Smith', '2003-03-22', 'F', 'jane.smith@example.com', '2345678901', '2022-01-15'),
            (3, 'Aarav', 'Kumar', '2001-11-10', 'M', 'aarav.kumar@example.com', '3456789012', '2020-09-10'),
            (4, 'Meera', 'Rao', '2002-07-19', 'F', 'meera.rao@example.com', '4567890123', '2021-07-20'),
            (5, 'Liam', 'Wilson', '2004-02-25', 'M', 'liam.wilson@example.com', '5678901234', '2023-02-01')
        ]

        # Insert the data
        cursor.executemany(insert_query, data_to_insert)
        connection.commit()
         
        cursor.execute("SELECT * FROM student")
        result = cursor.fetchall()
        print("All users:")
        for row in result:
            print(row)

finally:
    connection.close() 
    





    


