import mysql.connector
import pycountry

aConnection = mysql.connector.connect(user = 'root', 
                                      password = 'password', 
                                      host = '127.0.0.1')

# Get a list of country objects and creating a list of 3-letter countrycodes
country_codes_3 = []
countries = list(pycountry.countries)

for country in countries:
    country_codes_3.append(country.alpha_3)

print('\n\n')

while True:
    cCode = input('Please enter a country code:  ')
    cCode = cCode.upper()
    if cCode in country_codes_3:
        break

    print('Invalid Country code, please try again\n')

sql_sentense = f"SELECT District, Name FROM city WHERE CountryCode = '{cCode}';"

cursor = aConnection.cursor()

cursor.execute("USE world")
cursor.execute(sql_sentense)

# aConnection.commit()

databaseSelection = cursor.fetchall()

aConnection.close

cities = {}
for x in databaseSelection:
#    print(f"- {x[0]}\t{x[1]}")
    cities[x[0]] = x[1]

sorted_cities = dict(sorted(cities.items()))

# print(len(sorted_cities))
# print(type(sorted_cities))
# print()

print('\n\n')

for item in sorted_cities.items():
#    print(item)
    print(f"{item[0].rjust(30)}",end=' : ')
    print(f"{item[1].ljust(30)}")

# print(sorted_cities)

print()
print('--------------- : ---------------'.center(63))
print('End of print'.center(63))
print()
print()