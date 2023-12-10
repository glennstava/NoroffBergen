from objectsWithPython import *

first = Employee('Glenn', 1978)
second = Employee('james', 1954)

people = {'Hans' : 1964, 'Anders' : 1992, 'Jan' : 1975, 'Elizabeth' : 1951}
workers = []

for x in people.keys():
    teacher = Employee(x, people[x])
    workers.append(teacher)

for teac in workers:
    for key in teac.__dict__:
        print(f"{key} - {teac.__dict__[key]}")
    print('----\n')

# for attribute in dir(first):
#     print(attribute)

