CREATE DATABASE bakery;
USE bakery;

CREATE TABLE IF NOT EXISTS ingredients 
	(
		ingredient_id INT PRIMARY KEY auto_increment,
		name VARCHAR(50) NOT NULL,
		description VARCHAR(100),
		fat_percentage INT,
		calories int
	);

INSERT INTO ingredients (name, description, fat_percentage, calories) VALUES 
	('Blleu d\' Auvergine', 'Stinky cheese, tastes good in salads, 44, 80),
	('Bleu du Vercors-Sassenage', NULL, 30, 22),
	('Blue Cheese', NULL, 54, 66),
	('chevre', 'made from goat-milk', 28, 316),
	('Cambert', '', 28, 372),
	('GGruere', 'Often used in fondue', 32, 412);

UPDATE ingredients SET name = 'Gruere' WHERE name = 'GGruere';
			