# Create a script called MetricConverter.py. 
# In the script, create a function called metric_converter, 
# which receives a single numeric argument. 

# The purpose of this method is to receive a value in inches and then 
# convert it to centimetres. The function should display the number 
# of inches that it received and the number of centimetres after conversion. 
# The function shouldn’t return any values. 

# Demonstrate the use of the function in the main section of your script.
# --------------------------------------------------------------------------

# Conversion method
def metric_converter(number):
    print(f'Converting {number} inches to centimetres\n')
    return number * 2.45

# This method ensures that you have clean input
def inputChecker(measure):
    while True:
        variable = input(f'Please enter {measure}:  ')
        if variable.replace(".", "").isnumeric():
            variable = float(variable)
            break
        else:
            print('\nplease enter a real number:\n')

    return variable

def runProgram():
  
    while True:
        print('\n\n---- CONVERSION ----')

        var = inputChecker('number to be converted')
        print(f'Equals: {metric_converter(var)} Centimetres.\n\n')

        valg = input('Press enter to run again of Q to quit:  ')

        if valg.lower() == 'q':
            break

    input('\nPress enter to quit')

if __name__ == '__main__':
    runProgram()  
