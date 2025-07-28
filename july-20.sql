
SHOW DATABASES;


CREATE DATABASE IF NOT EXISTS employees;

USE employees;




CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100),
    phoneno BIGINT,
    salary DECIMAL(10, 2),
    city VARCHAR(100),
    bonus DECIMAL(10, 2)
);


INSERT INTO employees (name, department, phoneno, salary, city, bonus) VALUES
('alice', 'it', 1234567890, 56000.00, 'newyork', 5000),
('raj', 'civil', 2456178901, 45000.00, 'mayiladuthurai', 7000),
('saran', 'it', 5672891034, 40000.00, 'thajavur', 5000),
('sarmi', 'hr', 4536728196, 50000.00, 'trichy', 6000),
('praveena', 'it', 8610657843, 55000.00, 'madurai', 5000);

UPDATE employees
SET department = 'IT'
WHERE id = 6;



  select*from employees;
 


