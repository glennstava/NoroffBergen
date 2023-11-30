# Create a script called TimeCalculation.py. 
# A manager has requested that you write a script that allows him to enter a value 
# representing the number of minutes one of his employees has worked in a month. 

# He wants the script to use the number of minutes to calculate the number of days 
# worked in the month, the number of hours left over (not adding up to a full working day), 
# and the number of minutes left over (not adding up to a full hour). 

# For the sake of this calculation, a working day consists of eight hours. 
# Once calculated, display the resulting calculation 
# in the following format: working days:hours:minutes.

while True:
    totalMinutes = input('\nPlease enter how many minutes in total that you have worked?..  ')
    if totalMinutes.isnumeric():
        totalMinutes = int(totalMinutes)
        break
    else:
        print('\nWrong input value')

totalHours = totalMinutes // 60
totalDays = totalHours // 8

hoursLeft = totalHours - (totalDays * 8)
minutesLeft = totalMinutes - (totalHours * 60)

print(f'You have vorked totally {totalDays}:{hoursLeft}:{minutesLeft}\n\n')