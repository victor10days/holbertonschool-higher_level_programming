-- Script that creates a MySQL user --

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_3_pass';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
