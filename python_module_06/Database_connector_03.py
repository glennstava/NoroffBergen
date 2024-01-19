import mysql.connector
from pprint import pprint

con = mysql.connector.connect(user = 'root', 
                              password = 'password', 
                              host = '127.0.0.1')

selection = None
sql_get = "SELECT * FROM students;"

try:
    # Create a cursor object to interact with the database
    cursor = con.cursor()

    # Execute the update query
    cursor.execute("USE university")
    cursor.execute(sql_get)

    selection = cursor.fetchall()

except:
    print('Error')

finally:
    # Close the cursor and connection
    cursor.close()
    con.close()

if selection:

    print('Printing student list:')
    print('-'*30)
    print()

    for st in selection:
        print(f"Firet name  : {st[1]}")
        print(f"Family name : {st[2]}")
        print(f"E-mail      : {st[3]}")
        print()