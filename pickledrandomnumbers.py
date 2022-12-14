import random
import os
import pickle

'''
Create a script called pickledrandomnumbers.py. 
In this script, create a dictionary consisting of 26 alphabetic keys (a to z), 
each with an associated random number in the range 0 to 1000.
The script should only generate the random numbers 

if there is no pickle in which the dictionary is saved. 
If the dictionary already exists, load the data from the pickle. 
Display the dictionary to the user. 

Ask if the user wishes to update any of the entries. 
If "y", ask the user which entries they wish to update from a to z. 
Once the key has been selected, ask the user for a new numeric value to store with the key. 
If the dictionary has been updated, recreate the pickle.
'''

# Generate a random number
def randomNumber():
    tall = random.randint(0,1000)
    return tall

alphaDict = {}

for i in "abcdefghijklmnopqrstuvwxyz":
    alphaDict[i] = randomNumber()

# print(alphaDict)

if os.path.isfile("aPickle.dat"):
    print("Loading pickle")
    savedPickle = open("aPickle.dat","rb")

    exixtingPickle = pickle.load(savedPickle)
    savedPickle.close()
    print(exixtingPickle)

    while True:

        qu = input("Do you wishes to update any of the entries? (Y or N)  ")
        if qu.lower() == "y":

            entryToChange = input("Which entriy do you wish to update? (a to z)  ")
            if  entryToChange.lower() in exixtingPickle.keys():

                newEntry = input(f"Type the new value for {entryToChange}  ")
                exixtingPickle[entryToChange.lower()] = newEntry
            
            else:
                print("that entry is not in our dataset. try again\n")
        else:
            break

    alphaDict = exixtingPickle

print("Pickling the data")

newPickle = open("aPickle.dat","wb")
    
# Use the dump() method to save the data to the file
pickle.dump(alphaDict, newPickle)
newPickle.close()

print("\nprogram ended")