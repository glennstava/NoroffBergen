# Creating an empty list and filling the list with sets of numbers
numSets = []
for x in range(2,8):
    sets = set(range(x,1000,x))
    numSets.append(sets)

count = len(numSets)
combined = None

# Combining the lists
for x in range(count):

    if combined:
        newCombined = combined.intersection(numSets[x])
        combined = newCombined
        sortedset = sorted(combined)

    else:
        combined = numSets[x]

print(f'\nAll {x+2} meet for the first time after {sortedset[0]} days')
print('\n---------------\nEnd of script')