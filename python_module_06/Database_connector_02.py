import mysql.connector

con = mysql.connector.connect(user = 'root', 
                              password = 'password', 
                              host = '127.0.0.1')

fname = 'Ian'
lname = 'Gunneers'
email = 'ian.gunners@university.edu'

try:
    # Create a cursor object to interact with the database
    cursor = con.cursor()

    # Your SQL update statement
    sql_insert = f"INSERT INTO students (first_name, last_name, email) VALUES ('{fname}', '{lname}', '{email}');"

    # Execute the update query
    cursor.execute("USE university")
    cursor.execute(sql_insert)

    # Commit the changes to the database
    con.commit()
    
    print('Database updated')
    print(f"{cursor.rowcount} record(s) affected.")

finally:
    # Close the cursor and connection
    cursor.close()
    con.close()

print('\n----\nEnd os script')