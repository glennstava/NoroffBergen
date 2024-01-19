print('\nScript 01')

allMeet = []
for x in range(1,2001):
    if x % 2 == 0 and x % 3 == 0 and x % 4 == 0 and x % 5 == 0 and x % 6 == 0 and x % 7 == 0:
        allMeet.append(x)

print(f"They meet after {allMeet[0]} days")

print('\nScript 02')

x = 1
while True:
    if x % 2 == 0 and x % 3 == 0 and x % 4 == 0 and x % 5 == 0 and x % 6 == 0 and x % 7 == 0:
        print(f"They meet after {x} days")
        break
    x += 1
print('\nEnd of script\n\n')