'''
Option 4: 
Ask the user what number of the message data container they want to change. 
The user needs to enter a number from 0 to 3, 
and then the application needs to ask what the text for that index should be.

Once the text has been changed, 
the application must print the data container variable message to show 
that the text has been changed.
'''

messages = ['', '', '', '']

def addMessages():
#   global messages

    while True:
        messageNumber = input("\nplease enter a number, between 1 and 3: or press q to quit  ")

        if messageNumber.lower() == 'q':
            break

        # Checkingif the value is a number
        if messageNumber in ['0', '1', '2', '3']:
            messageNumber = int(messageNumber)

            aMessage = input("\nplease enter a short text: ")
            messages[messageNumber] = aMessage
            for m in messages:
                if m != '':
                    print(m)

        else:
            print("The entered value is invalid. Please try again\n")
            
    while True:
        valg = input("Print the stored massages? (y or n)  ")
        
        if valg.lower() in ['y', 'n']:

            if valg.lower() == 'y' and len(messages) != 0:
                for m in messages:
                    if m != '':
                        print(m)
            else:
                print('No messages to print')
            break

        else:
            print('Invalid selection, please try again\n')

    input('Press enter to continue')

