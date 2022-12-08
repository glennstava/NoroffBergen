# Displaying the menu

songs = ["A Hard Day's Night", 
"All You Need Is Love", 
"Blackbird", 
"Can't Buy Me Love", 
"Eight Days A Week", 
"Hello Goodbye", 
"Help!", 
"I Feel Fine", 
"Lady Madonna", 
"Let It Be", 
"Ob-La-Di, Ob-La-Da",
"Yesterday", 
"We Can Work It Out", 
"Hey Jude"
]

print("\n======= MENU =======")
print("Make a selection\n")

counter = 1
for song in songs:
    print(counter, "\t", song, sep="")
    counter += 1

while True:

    # try is to catch input errores to let the program keep running
    try:
        menuSelection = int(input("\nPlease select a menu option, or press 0 to exit...  "))

        # if 0 the program exits
        if menuSelection == 0:
            break

        # Checking if selection is valid
        if 1 <= menuSelection <= len(songs):

            print("Your Choice: \t", end="")
            print(songs[menuSelection - 1])

        # Number selected isn't within 1 - 8
        else:
            print("-- An invalid selection was entered --")

    # Bad input
    except:
        print("-- Enter a number between 1 and", len(songs))

print("\n---- Program ended ----")