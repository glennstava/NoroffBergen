for x in range(100, 0, -1):

    print(f'{x} bottles of beer on the wall.')
    print(f'{x} bottles of beer.') 
    print('Take one down, pass it around,')
    
    if x == 1:
        print("No more bottles of beer on the wall,")
        print()

        print("No more bottles of beer on the wall,")
        print("no more bottles of beer.")
        print("We've taken them down and passed them around;")
        print("now we're drunk and passed out!")

    else:
        print(f'{x-1} bottles of beer on the wall.')
        print()