two = set()
tree = set()
four = set()
five = set()
six = set()
seven = set()

all_3 = two.intersection(tree)
all_4 = all_3.intersection(four)
all_5 = all_4.intersection(five)
all_6 = all_5.intersection(six)
all_7 = all_6.intersection(seven)

print(all_7)