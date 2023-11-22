# Print out a house with 3 floors 
# -------------------------------

# parts that will be re-used
level = ' ' + '=' * 7 
floor = ' ' + '|' + ' ' * 5 + '|'

# printing Slanted roof
print(' ' * 4, end = 'A\n')
print(' ' * 3, end = '/X\\\n')
print(' ' * 2, end = '/XXX\\\n')
print(' ' * 1, end = '/XXXXX\\\n')

# printing a slab, 3 floors and an upper slab
print(level)
print(floor)
print(floor)
print(floor)
print(level)
