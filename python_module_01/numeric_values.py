# A way to verify that an input is numeric

value = input('Please enter a number between 1 and 10:  ')

if value.isnumeric():
    value = int(value)

    if value <= 0:
        print('too low')

    elif value < 4:
        print('Still very low')
    
    elif value < 6:
        print('average')
    
    elif value < 8:
        print('high')
    
    elif value <= 10 :
        print('Super')
    
    else:
        print('out of the chart')
    
else:
    print('invalid input')