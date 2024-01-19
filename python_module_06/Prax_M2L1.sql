/*
DROP DATABASE TekStore;
*/

CREATE DATABASE TekStore;
USE TekStore;

CREATE TABLE PostOffice 
(
	zipcode INT PRIMARY KEY,
	city VARCHAR(50) NOT NULL
);

CREATE TABLE Customers
(
	customer_id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(100) NOT NULL,
	address VARCHAR(200),
	zip INT,
	phone VARCHAR(20),
		CONSTRAINT fk_zip
		FOREIGN KEY (zip)
		REFERENCES PostOffice(zipcode)
			ON DELETE SET NULL
			ON UPDATE CASCADE
);

CREATE TABLE items
(
	item_id INT PRIMARY KEY AUTO_INCREMENT,
	item_name VARCHAR(100) NOT NULL,
	item_price INT NOT NULL
);

CREATE TABLE orders
(
	order_id INT PRIMARY KEY AUTO_INCREMENT,
	order_date DATE NOT NULL,
	customer INT NOT NULL,
	ordered_item INT NOT NULL,
	quantity INT NOT NULL DEFAULT 1,
		CONSTRAINT fk_customer
		FOREIGN KEY (customer)
		REFERENCES Customers(customer_id)
			ON DELETE RESTRICT
			ON UPDATE RESTRICT,
		CONSTRAINT fk_ordered_item
		FOREIGN KEY (ordered_item)
		REFERENCES items(item_id)
			ON DELETE RESTRICT
			ON UPDATE RESTRICT
);

INSERT INTO PostOffice (zipcode, city) VALUES
	(1746, 'Sarpsborg'),
	(5003, 'Bergen'),
	(3041, 'Drammen');

INSERT INTO Customers (name, address, zip, phone) VALUES
	('Marissa Prichard', 'Adolf Hedins vei 172', 1746, '420 86 786'),
	('Solveig Mikaelsson', 'Steinkjellerkroken 143', 5003, '945 07 718'),
	('Jannicke Wuopio', 'Hans Jægers vei 124', 3041, '458 49 439');

INSERT INTO items (item_name, item_price) VALUES 
	('Apple Iphone 6s 32GB', 9990), 
	('HTC U11 64GB', 5200),
	('Asus Zenfone 3 Max 32GB', 7390),
	('Sony Xperia XZ Premium 64GB', 8990),
	('Lenovo Moto G5 Plus 32GB', 5290);

INSERT INTO orders (order_date, customer, ordered_item) VALUES
	('2022-12-05', 1, 1),
	('2022-12-05', 2, 2),
	('2022-12-05', 3, 3),
	('2022-12-05', 1, 4),
	('2022-12-05', 2, 5);