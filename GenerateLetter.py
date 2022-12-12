'''
Create a script called GenerateLetter.py. 
Create a function called generate_letter which is to serve as a generator function. 
The generator should return a letter in the range a to e. 

If the generator returns the letter e, 
it should return the letter a the next time the generator function object is used. 

Demonstrate the use of the generator in the main portion of your script 
by display the letters a to e twice.
'''

def generate_letter():
    while True:
        for letter in "abcde":
            print(letter)
            yield

bokstav = generate_letter()

x = 0
while x < 12:
    next(bokstav)
    x += 1
