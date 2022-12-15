# A firefighter has 
#     name
#     surname 
#     staff number
#     age 
    
# There should also be a count field that keeps track of the number of firefighters in the system. 
# All firefighter instance variables/attributes should be initialised in the class constructor. 
# The total number of firefighters should also be incremented in the class constructor.

class FireFighter:
    staffcount = 0

    def __init__(self, name, surname, staffnumber, age):
        self.name = name
        self.surname = surname
        self.staffnumber = staffnumber
        self.age = age
        FireFighter.staffcount += 1

    def display(self):
        print(f"{self.staffnumber}:\t{self.surname}, {self.name} - age: {self.age}")