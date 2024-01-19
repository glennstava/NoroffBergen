CREATE TABLE Customers 
	(
		customer_id INT PRIMARY KEY AITO_INCREMENT, 
		surname VARCHAR(50) NOT NULL,
		initials VARCHAR(2),
		salutation CHAR(2),
		telnumber INT,
		address VARCHAR(100),
		email VARCHAR(100) 
	);

CREATE TABLE Orders
	(
		order_id INT PRIMARY KEY AUTO_INCREMENT, 
		order_date DATE NOT NULL,
		delivery_date DATE NOT NULL,
		customer INT NOT NULL
		total_price INT
			CONSTRAINT fk_customer
			FOREIGN KEY (customer)
			REFERENCES Customers(customer_id)
				ON DELETE RESTRICT
				ON UPDATE RESTRICT

	);



/*
INSERT the first 3 customers
*/

# First 3 Customers
# Remember that cust_id is an autoincrement field

INSERT INTO Customers (surname, initials, salutation, telnumber, address) VALUES
	("Haffa","JK","Mr", "004721689245", "Friggs vei 6, 4632, Kristiansand"),
	("Aagard","H","Dr", "004725763498", "Heimdalsgata 37, 0578, Oslo"),
	("Braaten","L","Ms", "004725896732", "Teglverksgata 11, 0553, Oslo");

# Insert an order for each customer
# Remember order_id is an autoincrement field

INSERT INTO Orders (order_date, delivery_date, customer, total_price) VALUES
	('20200131','20200210',1,399),
	('20200201','20200210',2,849),
	('20200201','20200213',3,799);


