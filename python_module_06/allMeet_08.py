x = 1
while True:
    if x % 2 == 0 and x % 3 == 0 and x % 4 == 0 and x % 5 == 0 and x % 6 == 0 and x % 7 == 0:
        print(f"They meet after {x} days")
        break
    x += 1

print('\nScript 2:')

x = 1
while True:
    if x % 2 == 0:
        if x % 3 == 0:
            if x % 4 == 0:
                if x % 5 == 0:
                    if x % 6 == 0:
                        if x % 7 == 0:
                            print(f"They meet after {x} days")
                            break
    x += 1

print('\nEnd of script\n\n')