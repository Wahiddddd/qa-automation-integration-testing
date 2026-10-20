CREATE DATABASE IF NOT EXISTS qa_integration;
USE qa_integration;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    role VARCHAR(50) NOT NULL
);

-- Data awal untuk skenario test retrieve by ID
INSERT INTO users (id, username, email, role) VALUES
(1, 'emilys', 'emily@test.com', 'buyer'),
(2, 'budi', 'budi@test.com', 'buyer'),
(3, 'andi', 'andi@test.com', 'admin')
ON DUPLICATE KEY UPDATE username=VALUES(username);