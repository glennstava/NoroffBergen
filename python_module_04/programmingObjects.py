# A class for a bird
class Bird:
    def __init__(self, name, color, species):
        self.name = name
        self.color = color
        self.species = species

    def sing(self):
        return f"{self.name} the {self.color} {self.species} is singing."

    def fly(self):
        return f"{self.name} the {self.color} {self.species} is flying."

# --------------------------------------

aBird = Bird("Polly", "Blue", "Parrot")

print(aBird.name)
print(aBird.color)
print(aBird.species)

print(aBird.sing())
print(aBird.fly())