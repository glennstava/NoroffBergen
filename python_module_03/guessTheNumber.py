'''
Option 1: 
The user needs to enter a number. 
The number needs to be assigned to a variable. 

If the number is equal to 543 then the application must print the words:
"You guessed the number! It is 543" 

If the number entered is lower than 543 then the application must print:
"The number you entered is too low"

If the number entered is higher than 543 then the application must print:
"The number you entered is too high"
'''
def guessNumber():
    aNumber = ""
    counter = 0
    while aNumber != "q":

        counter +=1
        aNumber = input("\nplease enter your number, or enter q to quit ")

        # Checkingif the value is a number
        if aNumber.isnumeric():
            aNumber = int(aNumber)

            if aNumber == 543:
                print("You guessed the number! It is 543")
                print("YOU ARE A WINNER!") 
                aNumber = "q"

            elif aNumber > 543:
                print("The number you entered is too high")

            else:
                print("The number you entered is too low")

        elif aNumber == "q":
            continue

        else:
            print("Value entered is wrong")

    print("\nProgram ended")
    pl = 's' if counter != 1 else ''

    print(f"Program ran {counter} time{pl}\n\n")
    input('Press enter to continue')