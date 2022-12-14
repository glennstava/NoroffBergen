'''
To run this code you must ensure to have foles available, or rename 
file-refferences to files that are available in your system
===================================================================  

# ---- File handeling ----
# Opens aNewFile.txt in writable mode. If the file doesn't exist, it is created

my_file = open("aNewFile.txt","w")

# The name property provides the file system name of the associated file
print("name: \t\t", my_file.name)

# The mode property provides details on which mode the file was opened as
print("mode: \t\t", my_file.mode)

# The closed property returns true if the file is closed
print("closed: \t", my_file.closed)

# The readable() method returns true if the file is readable
print("readable(): ", my_file.readable())

# The writable() method returns true if the file is writable
print("writable(): ", my_file.writable())
print()

# Closes the file to release the resources
my_file.close()

print("File methods and properties:")
print("closed: \t", my_file.closed)

# Once a file has been opened, it may be used to write content. 
# Once the file is then closed, the content may be read at a later stage, 

# -------- Writing to files --------

# To write to a file, the write() method is used.

my_file = open("thefile.txt","w")

# When writing to a file \n creates a new line 
write_me = "Raindrops on roses\nand whiskers on kittens,\nBright copper kettles\nand warm woolen mittens\n\n"
my_file.write(write_me)

# Lines can be written one at a time with the write()-method.  
my_file.write("Brown paper packages tied up with strings\n")
my_file.write("These are a few of my favorite things\n")
my_file.close()

# -------- Comma Separated files --------

my_file = open("aCSVfile.csv","w")

# First row - Headdings
my_file.write("Name,Work,Company,Debt\n")

# Next rows
my_file.write("Jimmy Jones, Msster cheff, Jimmys Tevern, 5000.00\n")
my_file.write("Gilbert Grape, Fruit dealer, Gilberts Apples and bolts, 40000.00\n")
my_file.write("Frida Frigg, Tinn food influenser, Stavanger Sardins factory, 190000.00\n")
my_file.close()

# -------- Reading files --------

# The file is opened using the readable mode
my_file = open("ATaleofTwoCities.txt","r")

# Display all the contents of the file
print(my_file.read())

# Using a for loop to display the contents line by line
for line in my_file:
    print(line)
    
my_file.close()

# -------- Tell() and Seek() --------

# We open a file in read mode
my_file = open("VivaLaVida.txt","r")

# Display all the contents of the file
print(my_file.read())
print()

print("Current pointer position", my_file.tell())

# Resetting position to 55
my_file.seek(55)

print("new current pointer position", my_file.tell())
print()

# Display the contents again starting at position 50.
# Only a portion of the file will be read.
for line in my_file:
    print(line, end="")

my_file.close()

# -------- Readlines --------

# By using the readlines() method, each line is read as an element in a list.

# The file is opened using the readable mode
my_file = open("MyFavoriteThings.txt","r")

# Using the readline() method to read all of a file's contents at once
songLyric = my_file.readlines()

print(songLyric)
print()

# The individual lines are stored as elements in a list

counter = 0
for line in songLyric:
    print(line, end="")

    counter += 1
    if counter > 10:
        break

my_file.close()

# -------- Apend files --------

# The file is opened using the readable mode
my_file = open("WeDidntStarttheFire.txt","a")

for i in range(0,4):
    # The write statement appends an extra line to the file.
    my_file.write("\nWe did infact, start a fire")

my_file.close()

# -------- using with and r+ / w+ mode --------

# We open the file in r+ mode
# When using with open, the file will be released as the block exits scope.
# without the need for a close() statement
with open("WinterWonderland.txt","r+") as my_file:
    
    # Move the file pointer to 77   
    my_file.seek(77)
    
    # Overwrite the text at file pointer 77
    my_file.write("  In the summertime, when the weather is high\nYou can stretch right up and touch the  ")
    
    # Return to the start of the file
    my_file.seek(0)

    # Display the file contents
    print(my_file.read())
    my_file.close()

# -------- using OS-method to remove a file --------

import os

# Creates an empty file and closes it
temp_file = open("tempfile.txt","x")
temp_file.close()

# Test if the file exists
if os.path.isfile("tempfile.txt"):

    # If it does, remove it
    print("File found - removing it.")
    os.remove("tempfile.txt")

# -------- Pickling --------

import pickle, os

# We loop the code three times. 
# In the first loop, the pickle won't initially exist.  
# It will be created at the end of the first loop.  
# The second loop will then load the data from the pickle 
# and save new data at the end of the loop.  
# This will continue for the third loop.

for runs in range(0,3):
    print("Loop", runs + 1)

    # Create a list with a few default values
    data = [1, 22, 333, 4444,]

    # Test if the pickle exists. If it exists it means the program has been run before 
    # and there is data to load. The if statement open the pickle file
    if os.path.isfile("mypickle.dat"):
        print("Loading pickle")
        the_saved_pickle = open("mypickle.dat","rb")
        
        # Use pickle to read the data from the file. This data was stored as a list, 
        # it will be loaded as a list.
        data = pickle.load(the_saved_pickle)
        the_saved_pickle.close()
    
    else:
        print("No pickle to load")

    print("Data before modification:")
    print(data)

    # Update the data
    for i in range(0,4):
        data[i] = data[i] + 1
    
    print("Data after modification:")
    print(data)
    
    print("Pickling the data")
    the_new_pickle = open("mypickle.dat","wb")
    
    # Use the dump() method to save the data to the file
    pickle.dump(data,the_new_pickle)
    the_new_pickle.close()
    print("-" * 30)
'''