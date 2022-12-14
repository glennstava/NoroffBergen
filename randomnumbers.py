import random

# Create a script called randomnumbers.py. 
# In the script, generate 100 random numbers in the range of 0 to 500. 

# Ask the user for a file name to which the random numbers should be saved. 
# Save the file to disk.

def randomNumber(maximum):
    randNum = random.sample(range(1, 500),maximum)
    randNum.sort()
    return randNum

tall = randomNumber(100)
randomLine = ""

fileName = input("write the name of your file:  ")
fileName += ".txt"

for i in tall:
    randomLine += str(i)
    randomLine += ","

with open(fileName,"w") as my_file:
    my_file.write(randomLine)
    my_file.close()