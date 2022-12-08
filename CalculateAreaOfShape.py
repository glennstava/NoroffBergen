'''
Create a script called CalculateAreaOfShape.py. 
In the script, create a function called calculate_area_of_shape. 

The function should receive five arguments. 
The first argument should define what shape's area needs to be calculated,
square, cube and circle
The other four arguments should be used to send measurements for 
length, height, width and radius. 

These four arguments should default to the value 0 if not used. 
Your function should calculate the area of at least three different shapes 

In the main section of your script, 
demonstrate the calculation of the area of three shapes. 
Your function calls should make use of named arguments.
'''
def calculate_area_of_shape(shape, length = 0, height = 0, width = 0, radius = 0):
    if shape == "square" or shape == "cube" or shape == "circle":
        if shape == "square":
            if length > 0 and width > 0:
                print("The square is:", length * width)
            else:
                print("Parametres missing. The square cannot be calculated")
    
        elif shape == "cube":
            if length > 0 and width > 0 and height > 0:
                print("The cube is:", length * width * height)
            else:
                print("Parametres missing. The cube cannot be calculated")

        else:
            if radius > 0:
                print("The area of the circle is:", 3.14 * radius ** 2)
            else:
                print("Parametres missing. The area of the circle cannot be calculated")
    else:
        print("Shape missing or unknown. Cannot be calculated")

calculate_area_of_shape("circle")
# calculate_area_of_shape("square",5)
# calculate_area_of_shape("cube",5,5,5)

