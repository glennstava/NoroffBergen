import mysql.connector
from pprint import pprint;

aConnection = mysql.connector.connect(user = 'root', password = 'password', host = '127.0.0.1')

cursor = aConnection.cursor()
cursor.execute("USE personel")

name = input("enter username:  ")
pwprd = input("enter password:  ")

sql_sentense = f"select name from login where user_name = '{name}' and password = '{pwprd}';"
# print(sql_sentense)

cursor.execute(sql_sentense)
aConnection.commit()

pprint(cursor.fetchall())

aConnection.close