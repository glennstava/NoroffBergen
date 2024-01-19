create table car 
(
	id int primary key auto_increment, 
	brand varchar(50) unique not null, 
	price int not null
);

create table car_orders 
(
	order_id int primary key auto_increment, 
	carid int not null, 
	order_date date not null, 
	total_price int not null, 
		CONSTRAINT fk_carid
		FOREIGN KEY (carid)
		REFERENCES car(id)
				ON DELETE RESTRICT
				ON UPDATE RESTRICT
);

Insert into car (brand, price) values 
	('volvo', 390000),
	('Ford', 450000),
	('Nissan', 490000),
	('Toyota', 50000),
	('BMW', 880000),
	('VW', 450000),
	('Suzzuki', 290000),
	('Porche', 980000);

select * from car;
+----+---------+--------+
|  1 | volvo   | 390000 |
|  2 | Ford    | 450000 |
|  3 | Nissan  | 490000 |
|  4 | Toyota  |  50000 |
|  5 | BMW     | 880000 |
|  6 | VW      | 450000 |
|  7 | Suzzuki | 290000 |
|  8 | Porche  | 980000 |
+----+---------+--------+

Insert into car_orders (carid, order_date, total_price) values 
	(1, '2022-01-18', 350000),
	(3, '2022-01-15', 480000),
	(8, '2022-01-21', 890000),
	(7, '2022-01-12', 200000),
	(1, '2022-01-11', 340000),
	(2, '2022-01-26', 480000),
	(1, '2022-01-29', 400000),
	(7, '2022-01-23', 200000);

select * from car_orders;
+----------+-------+------------+-------------+
| order_id | carid | order_date | total_price |
+----------+-------+------------+-------------+
|        1 |     1 | 2022-01-18 |      350000 |
|        2 |     3 | 2022-01-15 |      480000 |
|        3 |     8 | 2022-01-21 |      890000 |
|        4 |     7 | 2022-01-12 |      200000 |
|        5 |     1 | 2022-01-11 |      340000 |
|        6 |     2 | 2022-01-26 |      480000 |
|        7 |     1 | 2022-01-29 |      400000 |
|        8 |     7 | 2022-01-23 |      200000 |
+----------+-------+------------+-------------+

select sum(total_price) AS 'Totalt salg' from car_orders where carid = 1
select round(avg(total_price)) AS 'Snitt pris' from car_orders where carid = 1

select min(total_price) AS Lavest from car_orders;
select max(total_price) AS Høyest from car_orders;






	 