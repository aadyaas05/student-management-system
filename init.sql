CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    course VARCHAR(50)
);

INSERT INTO students (name, email, course) VALUES
('Alice', 'alice@example.com', 'CSE'),
('Bob', 'bob@example.com', 'IT'),
('Charlie', 'charlie@example.com', 'ECE');
