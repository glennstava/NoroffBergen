from checkInTime import timeCheck
from guessTheNumber import guessNumber
from MessageInABox import printMessage
from messageContainer import addMessages

line = '-' * 30
games = ['Guess the number', 'Calculate time', 'Print something', 'Change a print option'] 

# Setting up the menu in the program

def showMenu(gameList):
    print('\n\n')
    print(line)
    print('Menu System')
    print(line) 
    print()

    for num, game in enumerate(gameList, start = 1):
        print(f'{num} - {game}')
        print()

    print(line) 
    print()

# ---------
# Start of program

def runProgram():
    
    showMenu(games)

    while True:
        choice = input('Make a selection, or press q to quit\nor press m to see the Menu again:  ')
        
        if choice.lower() == 'q':
            break

        if choice.lower() == 'm':
            showMenu(games)
            print()
        
        elif choice.isnumeric() and int(choice) -1 in range(len(games)):
            choice = int(choice) - 1

            if choice == 0:
                guessNumber()
                print()

            if choice == 1:
                timeCheck()
                print()

            if choice == 2:
                printMessage()
                print()

            if choice == 3:
                addMessages()
                print()

        else:
            print('Invalid input\n') 


if __name__ == '__main__':
    runProgram()

    print()
    print('.' * 20)
    print('program ended\n\n')