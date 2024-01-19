two = set(range(2,1000,2))
tree = set(range(3,1000,3))
four = set(range(4,1000,4))
five = set(range(5,1000,5))
six = set(range(6,1000,6))
seven = set(range(7,1000,7))

all_3 = two.intersection(tree)
all_4 = all_3.intersection(four)
all_5 = all_4.intersection(five)
all_6 = all_5.intersection(six)
all_7 = all_6.intersection(seven)

print(sorted(all_7))