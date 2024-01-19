# The first guy is there every day, we can thus ignore him
# So we make a set for every range
two = set()
tree = set()
four = set()
five = set()
six = set()
seven = set()

# We'll fill up the sets hoping we'll have a match within the first 900
for x in range(1,901):
    if x % 2 == 0:
        two.add(x)
    if x % 3 == 0:
        tree.add(x)  
    if x % 4 == 0:
        four.add(x)
    if x % 5 == 0:
        five.add(x)
    if x % 6 == 0:
        six.add(x)
    if x % 7 == 0:
        seven.add(x)

        
# A setcannot contain duplicates
# The intersection-function gives us the matches
all_3 = two.intersection(tree)
all_4 = all_3.intersection(four)
all_5 = all_4.intersection(five)
all_6 = all_5.intersection(six)
all_7 = all_6.intersection(seven)

# Printing the one we want
print(all_7)