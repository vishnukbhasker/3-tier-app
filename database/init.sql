<!-- database/init.sql -->
CREATE DATABASE IF NOT EXISTS users_db;
USE users_db;
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT
);
