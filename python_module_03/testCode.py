
from checkInTime import timeCheck
from guessTheNumber import guessNumber
from MessageInABox import printMessage
from messageContainer import addMessages

def aFiftGame():
    print('Hei 5')

def aSixtGame():
    print('Hei 6')

gamedict = {'Guess the number' : guessNumber, 
            'Calculate time' : timeCheck, 
            'Print something' : printMessage, 
            'Change a print option' : addMessages,
            'Game 5' : aFiftGame,
            'Game 6' : aSixtGame}

newGames = list(gamedict.keys())
newFunc = list(gamedict.values())

line = '-' * 30

print('\n\n')
print(line)
print('Menu System')
print(line) 
print()

for num, game in enumerate(newGames, start = 1):
    print(f'{num} - {game}')
    print()

print(line) 
print()


while True:
    choice = input('Make a selection, or press q to quit:  ')
    
    if choice.lower() == 'q':
        break
    
    if choice.isnumeric() and int(choice) -1 in range(len(newGames)):
        choice = int(choice) - 1

        gameToRun = newFunc[choice]()  
        gameToRun
        print()
    
    else:
        print('Invalid input\n') 