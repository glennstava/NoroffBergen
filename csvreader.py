# Open up a spreadsheet editor and create a CSV file called mycsv.csv. 
# Populate this file with data as you choose. 

# Create a script called csvreader.py. 
# Load the data from the mycsv.cvs file and display it to the user.

with open("MockData_01.csv","r") as aFile:
    readFile = aFile.readlines()
    
    # The individual lines are stored as elements in a list
    for line in readFile:
        print(line, end="")
    
    aFile.close()

