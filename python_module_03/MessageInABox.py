'''
Option 3: 
The end user must enter a number between 0 and 3. 
For each number the application must print a message that is 
associated with that number from the given data container below: 

If the user enters 2, the application must print the words: 
"We learn Python the fun way"
'''

message = ["Coding is fun", 
            "Python is not code, but a way of life", 
            "We learn Python the fun way", 
            "We code, because we can"] 

def printMessage():

    while True:
        aNumber = input("\nplease enter number between 0 and 3 or enter q to quit ")

        if aNumber.lower() == 'q':
            break

        # Checkingif the value is a number
        if aNumber.isdigit():
            aNumber = int(aNumber)
            
            if 0 <= aNumber <=3:
                print(message[aNumber])
            
            else:
                print(f"Option {aNumber} is not in our system")
        else:
            print("The value entered is incorrect. please try again\n")

    input('\nPress enter to continue')

if __name__ == '__main__':
    printMessage()