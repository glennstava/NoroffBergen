'''
Option 2
Write a python script that will confirm if a time entered by the end user is between 
08h00 in the morning and 17h00 in the afternoon. 

If the time is between these two values, 
the application must display the word “It is working hours still”. 

If the time is not within these two times, 
the application must display the words “Please do not work anymore, it is personal time now”
'''

def timeCheck():
    while True:    
        timeEntered = input("Enter time: (format hh:mm) or press q to quit:  ")

        # program exits with q as an input
        if timeEntered.lower() == 'q':
            break

        # To ensure that the data enterd is correct
        #  - input is exactly 5 characters
        #  - 3. character (index 2) equals ":"
        #  - first 2 characters is digits
        #  - last 2 characters is digits
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

                break

            # Timeformat is wrong
            else:
                print("Data entered is in the wrong format. (code 02)\n- please try again\n")

        # Timeformat is wrong
        else:
            print("Data entered is in the wrong format. (code 01)\n- please try again\n")

    input('\npress enter to continue')

if __name__ == '__main__':
    timeCheck()