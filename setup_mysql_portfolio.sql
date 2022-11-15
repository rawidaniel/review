-- prepares a MySQL server for the portfolio project
DROP DATABASE IF EXISTS hbnb_addis_review_db;
CREATE DATABASE IF NOT EXISTS hbnb_addis_review_db;
USE hbnb_addis_review_db;
CREATE USER IF NOT EXISTS 'hbnb_addis_review'@'localhost' IDENTIFIED BY 'addisreview';
GRANT ALL PRIVILEGES ON hbnb_addis_review_db.* TO 'hbnb_addis_review'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_addis_review'@'localhost';
