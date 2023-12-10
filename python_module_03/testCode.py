from checkInTime import timeCheck
from guessTheNumber import guessNumber
from MessageInABox import printMessage
from messageContainer import addMessages

gamedict = {'Guess the number' : guessNumber, 
            'Calculate time' : timeCheck, 
            'Print something' : printMessage, 
            'Change a print option' : addMessages}

games = list(gamedict.keys())
newFunc = list(gamedict.values())

def showMenu(gameList):
    line = '-' * 30
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

            gameToRun = newFunc[choice]()  
            gameToRun
            print()

        else:
            print('Invalid input\n') 


if __name__ == '__main__':
    runProgram()

    print()
    print('.' * 20)
    print('program ended')
    input('Press Enter\n\n')
