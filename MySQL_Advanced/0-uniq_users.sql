-- Script to create a "users" table

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
