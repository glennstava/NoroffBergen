LOAD DATA LOCAL INFILE
'C:\\Users\\glenn\\OneDrive\\Dokumenter\Noroff\Databases\Population-change.csv"
INTO TABLE population_change
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS