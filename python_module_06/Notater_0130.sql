create database buttonstore;
use buttonstore;
create table buttons 
(
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(100),
    price INT NOT NULL
);

SELECT name, price AS 'Stykkpris', price * 4 AS 'Totalpris' 
FROM buttons ORDER BY price DESC LIMIT 3;

SHOW GLOBAL VARIABLES LIKE 'local_infile';
set global local_infile=true;
