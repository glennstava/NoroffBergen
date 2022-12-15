'''
Create a module file called rectangle.py
create a class called rectangle. 
A rectangle should have instance variables for 
length, width and display_character. 
These variables should be initialised in the constructor. 

A method called calculate_area() returning its area.
A method called display, which will display the length, width and the area.

This method should also draw the rectangle to screen using the display_character, e.g. 
for a rectangle with a length of 6, the width of 3 and a display_character of *; 
it will look as follows:
'''

class RecTAngle:
    length = None
    width = None
    display_character = None

    def __init__(self, length, width, display_character):
        self.length = length
        self.width = width
        self.display_character = display_character
    
    def calculate_area(self):
        return self.length * self.width
    
    def draw_rectangle(self):
        for i in range(self.width):
            print()
            for j in range(self.length):
                print(self.display_character, end="")

    def display(self):
        print(f"Rectangle - length: {self.length}, width: {self.width}, area: {self.calculate_area()}")
        self.draw_rectangle()