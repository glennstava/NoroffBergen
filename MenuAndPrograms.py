# The Menu and programs script is building upon Lesson task
# 3.2 Performing operations from Xlyme - Moodle
# The functionality have been extended with methods from all
# the lessons up untill 3.4
# # ========================================================

# First we declare a function for the Guess a number task
def guessTheNumber():
    aNumber = ""
    counter = 0

    # Eternal loop will break only when user enters q (Break is initiated)
    while True:

        counter +=1
        aNumber = input("\nplease enter your number, or enter q to quit ")

        # Checkingif the value is a number
        if aNumber.isdigit():
            aNumber = int(aNumber)

            # three statements thet is the game
            if aNumber == 543:
                print("You guessed the number! It is 543")
                print("YOU ARE A WINNER!") 
                break

            elif aNumber > 543:
                print("The number you entered is too high")

            else:
                print("The number you entered is too low")

        # The statement to break the loop
        elif aNumber.lower() == "q":
            break

        # For the program to continue even if an elegal value is entered    
        else:
            print("Value entered is wrong")

    # After the loop and the program has finished - this is displayed
    print("\nProgram ended")
    print("Program ran for ", counter, " times",sep="")

    # This statement is for the program to pause before 
    input("press any key to exit ")

# # ========================================================

# We declare a function for the program to determine if 
# you're within your working time
def calculateTime():

    # Eternal loop will break only when user enters q (Break is initiated)
    while True:

        timeEntered = input("\nEnter time (format hh:mm) or press q to exit ")

        # first part is to ensure that the data enterd is correct
        if len(timeEntered) == 5 and timeEntered[2] == ":" and timeEntered[:2].isdigit() and timeEntered[3:].isdigit():

            # To simplify we are naming the first 2 digits hour and the second 2 minutes 
            hour = int(timeEntered[:2])
            minutes = int(timeEntered[3:])

            # Is hours between 0 - 24 and minutes between 0 - 59
            if 0 <= hour <= 23 and 0 <= minutes <= 59:

                # The actual timecheck
                if 8 <= hour < 17:
                    print("It is working hours still")
                else:
                    print("Please do not work anymore, it is personal time now")
        
            # Timeformat is wrong
            else:
                print("\nData entered is in the wrong format. (code 02)")

        # The statement to break the loop
        elif timeEntered.lower() == "q":
            break
        
        # Timeformat is wrong
        else:
            print("\nData entered is in the wrong format. (code 01)")

# # ========================================================

# We declare a function for the Message in a box program
def messageInABox():
    
    # A list is declared with the messages the program uses 
    message = ["Coding is fun", 
            "Python is not code, but a way of life", 
            "We learn Python the fun way", 
            "We code, because we can"
    ]

#    aNumber = 1
    # Eternal loop will break only when user enters q (Break is initiated)
    while True:
        aNumber = input("\nplease enter number between 1 and 4 or enter q to quit ")

        # Checkingif the value is a number
        if aNumber.isdigit():
            aNumber = int(aNumber)

            if 1 <= aNumber <=4:
                print(message[aNumber-1])
        
            else:
                print("Option ", aNumber, " is not in our system",sep="")

        # The statement to break the loop
        elif aNumber.lower() == "q":
            break
        
        else:
            print("The value entered is incorrect")

# # ========================================================

# We declare a function for messagelist
def messageList():

    # An empty list is declered 
    messages = ["", "", "", ""]

    # Eternal loop will break only when user enters q (Break is initiated)
    while True:
        messageNumber = input("\nplease enter a number, between 0 and 3: or press q to quit ")

        # Checkingif the value is a number
        if messageNumber.isdigit():
            messageNumber = int(messageNumber)

            if 0 <= messageNumber <=3:
                aMessage = input("\nplease enter a short text: ")
                messages[messageNumber] = aMessage
                print(messages)

            else:
                print("The number entered is wrong")
        
        # The statement to break the loop
        elif messageNumber.lower() == "q":
            break

        else:
            print("The entered value is wrong")

    # After the loop and the program has finished - this is displayed
    print("\nThe final list")

    # prints the final result
    for item in enumerate(messages,1):
        print(item, end=" ")

    # This statement is for the program to pause before 
    input("press any key to exit ")

# # ========================================================

# The main program starts here
while True:

    # ==========
    # Main menu
    # ==========

    print()
    print("-" * 34)
    print("Menu System")
    print("-" * 34)
    print("\nPlease select one of these numbers")
    print("\n1.\tGuess the number")
    print("2.\tCalculate time ")
    print("3.\tPrint something")
    print("4.\tChange a print option\n")
    print("-" * 34)

    selection = input("\nMake a sellection, or press q to quit: ")
    if selection.isdigit():
        selection = int(selection)

        if 1 <= selection <= 4:
            
            if selection == 1:
                guessTheNumber()
            
            elif selection == 2:
                calculateTime()

            elif selection == 3:
                messageInABox()
            
            else:
                messageList()
        
        else:
            print("Option", selection, "is not in our system")

    # The statement to break the loop    
    elif selection == "q":
        break
    
    else:
        print("Value entered is incorrect")

# Statement printed when program ends
print()
print("-" * 20)
print("Program ended\n")