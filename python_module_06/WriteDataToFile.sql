select * from population_change
INTO OUTFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\New-Population-change.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'

LOAD DATA LOCAL INFILE
'C:\\Databases\\population-change.csv'
INTO TABLE population_change
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

