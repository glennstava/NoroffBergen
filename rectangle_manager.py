import Rectangle as firkant
'''
Create a script called rectangle_manager.py. 
In this script, import the rectangle module. 

Ask the user to enter the details of rectangles
length, width and display_character 

The user should be able to enter as many rectangles as they wish. 
As each rectangle is created, store the created rectangles in a list. 
Once the user is happy that they have created enough rectangles, 
they should be allowed to stop entering rectangles. 

The script should then display the details of each saved rectangle 
to the console window.
'''

firkantList = []

while True:

    cont = input("\nPress y to create a rectangle:  ")

    if cont.lower() == "y":
#        try:
        lengde = int(input("type the length of your rectangle:  "))
        bredde = int(input("type the width of your rectangle:  "))
        tegn = input("type a single display character:  ")

        rectangle = firkant.RecTAngle(lengde, bredde, tegn)
        firkantList.append(rectangle)

#        except:
#            print("wrong input")
    else:
        break

input("Press enter to continue")

for item in firkantList:
    item.display()
    print()
