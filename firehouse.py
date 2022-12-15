import Firefighter as brannmann

# Create a script called firehouse.py. 
# In this script, you must import the firefighter's module and create at least three different firefighters. 
# Display the details of the three firefighters to the console window 
# along with the total number of firefighters created (using a class variable).

fireguard_01 = brannmann.FireFighter("Petter", "Pyro", 48001, 22)
fireguard_02 = brannmann.FireFighter("Finn", "Flammered", 48002, 19)
fireguard_03 = brannmann.FireFighter("Gerd", "Gal", 48010, 25)

fireguard_01.display()
fireguard_02.display()
fireguard_03.display()

print("\nStaffcount:", brannmann.FireFighter.staffcount)
print("\nStaffcount:", fireguard_03.staffcount)
