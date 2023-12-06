# Create a script called CalculateVolume.py. 
# An engineer wants to calculate the volume of a rectangular tank using 
# the formula length width height. 

# The program needs to request these three values as input from the user 
# and store them in three different variables. 

# Using these three variables, calculate the volume of the tank 
# and store it in a fourth variable. 

# The engineer has learnt from experience that measurements and calculations 
# are always a bit short of the volume the tank can store because the plastic 
# tank expands when filled. 
# Therefore, he requires that the script increase the calculated 
# volume of the tank by 1% before displaying the resulting volume to the user.
# ----------------------------------------------------------------------------

def inputChecker(measure):
    while True:
        variable = input(f'please enter {measure}:\t')
        if variable.replace(".", "").isnumeric():
            variable = float(variable)
            break
        else:
            print('\nplease enter a real number:\n')

    return variable

def VolumeCalculate():
    length = inputChecker('Length')
    width = inputChecker('Width')
    height = inputChecker('Heigth')

    volume = length * width * height
    truevolume = volume * 1.01

    print(f'\nThe volume of the box is: {volume} cubic')
    print(f'The true volume of the box is: {truevolume} cubic\n\n')

if __name__ == '__main__':
    VolumeCalculate()