bottles = open("Bottles_of_beer.txt","w")

lines = "100 Bottles of beer on the wall\n\n\n"
bottles.write(lines)

for x in range(100, 0, -1):

    bottles.write(f'{x} bottles of beer on the wall.\n')
    bottles.write(f'{x} bottles of beer.\n') 
    bottles.write('Take one down, pass it around,\n')
    
    if x == 1:
        bottles.write("No more bottles of beer on the wall,\n")
        bottles.write('\n\n')

        bottles.write("No more bottles of beer on the wall,\n")
        bottles.write("no more bottles of beer.\n")
        bottles.write("We've taken them down and passed them around;\n")
        bottles.write("now we're drunk and passed out!\n")

    else:
        bottles.write(f'{x-1} bottles of beer on the wall.\n')
        bottles.write('\n\n')

bottles.close()

print('--\nScript finished')