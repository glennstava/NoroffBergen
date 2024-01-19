import mysql.connector

con = mysql.connector.connect(user = 'root', 
                              password = 'password', 
                              host = '127.0.0.1')

sql_query = f"SELECT CountryCode FROM city;"

cursor = con.cursor()

cursor.execute("USE world")
cursor.execute(sql_query)

result = cursor.fetchall()

cCodes = set()

for x in result:
    cCodes.add(x[0])

listCodes = list(cCodes.copy())
listCodes.sort()

print(listCodes)
print(len(listCodes))

print('\n----\n')

for x in listCodes:
    if len(x) != 3:
        listCodes.remove(x)

print(listCodes)
print(len(listCodes))

