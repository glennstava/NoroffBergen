'''
Create a script called SummingMachine.py. 
In the script, create a function called summing_machine. 
The function should receive no argument. 

It should continuously ask the user to enter a number 
until they enter 's' to stop, 
The values entered must be added together, and the final result 
returned to the calling code. 

Demonstrate the use of the function in the main section of your script.
'''

def summing_machine():
    
    totalValue = 0

    while True:
        value = input("Type a value: ")

        if value.isdigit():
            value = float(value)
            totalValue += value

        elif value.lower() == "s":
            break

        else:
            print(value, "Cannot be used in calculation\n")
    
    return totalValue

print("Using summing machine")
sum = summing_machine()

print("\nProgrem terminated \nFinal sum:", sum, "\n")