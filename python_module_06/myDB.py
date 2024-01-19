import myDBconfig as myDB
from pprint import pprint;
import mysql.connector as mysql

conn = mysql.connect(**myDB.dbConfig)

cursor = conn.cursor()
cursor.execute("USE university")
'''
try:
    cursor.execute("INSERT INTO offerings (course_code, start_date) VALUES ('SQL2', '20200412')")
    conn.commit()
    
    cursor.execute("SELECT * FROM offerings")
    pprint(cursor.fetchall())

except mysql.Error as err:
    if err.errno == 1452:
        print('Course code does not exist')
    else:
        raise

conn.close

cursor.execute("INSERT INTO students (first_name, last_name, email) VALUES ('Harry', 'Franzen', 'dynamitt@olsenbanden.no')")


cursor.execute("SELECT * FROM students")





# cursor.execute("USE university")
# cursor.execute("INSERT INTO students (first_name, last_name, email) VALUES ('Solan', 'Gundersen', 'solan.gundersen@flaaklypatidene.no')")
# cursor.execute("INSERT INTO students (first_name, last_name, email) VALUES ('Ludvig', 'Pelsen', 'ludvig.pelsen@flaaklypatidene.no')")
# cursor.execute("INSERT INTO students (first_name, last_name, email) VALUES ('Reodor', 'Felgen', 'reodor.felgen@iltempogigante.no')")

# cursor.execute("INSERT INTO students (first_name, last_name, email) VALUES ('Egon', 'Olsen', 'egon@olsenbanden.no')")
# cursor.execute("INSERT INTO students (first_name, last_name, email) VALUES ('Benny', 'Franzen', 'bennyludvig@olsenbanden.no')")
# cursor.execute("INSERT INTO students (first_name, last_name, email) VALUES ('Kjell', 'Jensen', 'kjell@olsenbanden.no')")
'''


sql_command = """INSERT INTO students (first_name, last_name, email) VALUES 
                            ('Per', 'Holms', 'holms@politiet.no');"""
cursor.execute(sql_command)
conn.commit()

cursor.execute("SELECT * FROM students")
pprint(cursor.fetchall())

conn.close

