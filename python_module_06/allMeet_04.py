# Creating an empty list and filling the list with sets of numbers

numSets = []
for x in range(2,8):
    sets = set(range(x,1000,x))
    numSets.append(sets)

combined = None

# Combining the sets
for x in range(len(numSets)):

    if combined:
        newCombined = combined.intersection(numSets[x])
        combined = newCombined

    else:
        combined = numSets[x]
    
sortedset = sorted(combined)

print(f'\nAll {x+2} meet for the first time after {sortedset[0]} days')
print('\n-------------\nEnd of script')