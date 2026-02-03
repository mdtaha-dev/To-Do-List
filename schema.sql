CREATE DATABASE toDo;
USE toDo;

CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(50) NOT NULL,
    description TEXT,
    status ENUM('pending', 'completed') DEFAULT 'pending',
    task_created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

select * from tasks;