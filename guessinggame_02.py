from time import *
import random
'''
Modified version of guessing programe from Xlyme 4.2
where all metodes are in the same file
'''
# Generate a randome numbre
def randomNumber(maximum):
    tall = random.randint(0, maximum)
    return tall

# The guellinggame program
def guessingNumber():

    # Sets a start time to time how long the game is running
    start = time()
    gameStart = localtime(start)
    
    while True:
        # To break the while-loop and stop the program
        again = input("Press N to quit, or any other key to continue  ")
        if again.lower() == "n":
            break
        
        # We use a try . exsept to hinder bad input from chrashing the program
        try:
            aNumber = int(input("\nGuess a number between 0 and 10  "))
            
            # only numbers between 0 and 10 are valid input 
            if 0 <= aNumber <= 10:
                rightNumber = randomNumber(10)

                if aNumber == rightNumber:
                    print("Congratulation your gues was correct")
                    print("You are a winner\n")

                else:
                    print("Unfortunatly your guess was incorrect")
                    print("your guess was: ", aNumber)
                    print("The right number was:", rightNumber)

            else:
                raise ValueError()   
#                print("your guess should be between 1 and 10. Try again\n")
               
        except:
            print("Wrong input. Your guess should be between 1 and 10.\n")
    
    end = time()
    timeDifference = end - start

    print("\nThe Guessing Game ended")
    print("You played the game for", round(timeDifference,), "seconds.")
    print()

guessingNumber()