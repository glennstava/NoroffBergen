"""
Create a function named divide, 
which has the following details:

It needs to receive 2 parameters.

The first parameter should be divided by the second one.

The function should return the result of 
the division as an integer.

If the result is less than 0, 
the function should return a value of 0.

If any errors occur during division, 
the function should return a value of -1
"""

def devide(num_01, num_02):
    result = 0
    try:
        result = num_01 / num_02

        if result < 0:
            result = 0

    except:
        result = -1

    return int(result)

print(devide(25,5))
print(devide(25,'dag'))
print(devide(25,-5))