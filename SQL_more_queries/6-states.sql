-- Script that creates database and table
CREATE DATABASE IF NOT EXISTS hbtn_04_usa;
USE hbtn_04_usa;
CREATE TABLE IF NOT EXISTS states (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(256) NOT NULL
);
