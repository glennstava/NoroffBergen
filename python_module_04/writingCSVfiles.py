from random import choice

def generateCar(number):
    carlist = []

    for i in range(number):
        car = {}
        car["type"] = choice(["Ford", "Volvo", "Peugot", "Nissan"])
        car["engine"] = choice(["petrol", "electric", "hydrogen"])
        car["colour"] = choice(["red", "blue", "white", "brown", "grey"])

        carlist.append(car)
    
    return carlist

cars = generateCar(10)
# print(cars)

carStock = open("New_Cars.csv","w")

# First row / heading
taglist = list(cars[0].keys())
tags = ','.join(taglist)
carStock.write(tags)
carStock.write('\n')

# The other rowes
for aCar in cars:
    speclist = list(aCar.values())
    spec = ','.join(speclist)
    carStock.write(spec)
    carStock.write('\n')

print('\n----\n')
print(f"Position {carStock.tell()}")

print("Resetting position to 0")
carStock.seek(0)
print('\n----\n')

# readline is used to read all of a file's contents at once
file_contents = carStock.readlines()
print(file_contents)
print()

# The individual lines are stored as elements in a string-based list
for line in file_contents:
    print(line,end="")

carStock.close()

print('End of script')