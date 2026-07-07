-- WEEK-II: PostgreSQL schema example with JOINs

CREATE TABLE departments (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL
);

CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    department_id INT NOT NULL REFERENCES departments(department_id)
);

INSERT INTO departments (department_name) VALUES
('Engineering'),
('Sales'),
('HR');

INSERT INTO employees (first_name, last_name, department_id) VALUES
('Alice', 'Johnson', 1),
('Bob', 'Lee', 1),
('Cathy', 'Nguyen', 2),
('David', 'Patel', 3);

-- Join departments and employees to show full employee details with department name
SELECT
    e.employee_id,
    e.first_name,
    e.last_name,
    d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id
ORDER BY e.employee_id;
