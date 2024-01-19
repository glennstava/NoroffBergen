# A fishingclub have 7 members
# Member 1 fishes every day
# Member 2 fishes every second day
# Member 3 fishes every third day, and so for forth.
# How many days until all members meet to fish on the same day?  
# ----------------------------------------------------------------

# We can ignore member one that is there every day.
# we need 6 lists that follows the multiplication table

# Creating an empty list and filling the list with sets of numbers
numSets = []
for x in range(2,8):             # 6 lists starting at 2 up to/including 7
    sets = set(range(x,1000,x))  # Create a set from x until 1000 each step is x   
    numSets.append(sets)         # Sets are added to the numSets-list

combined = None                  # Empty object to begin with

# Combining the lists
for x in range(len(numSets)):    # x will start at 0 and end at 5

    if combined:
        newCombined = combined.intersection(numSets[x])
        combined = newCombined

    else:
        combined = numSets[x]    # combined is set to the first list 

# The result-set sorted to make sure we get the smalest number as the first day 
sortedset = sorted(combined)

# x is 5 after the for-loop by adding 2 the text makes sense
# In case the resulting list have more than one value, we only want the first
print(f'\nAll {x+2} meet for the first time after {sortedset[0]} days')

# Ekstra lines to prettifu the output
num = sortedset[0]
year = num // 365
rest = num - (year * 365)
month = rest // 30
days = rest - (month * 30)

print(f'It will be {year}', end=' ')
print('years', end=', ') if year != 1 else print('year', end=', ')
print(month, end=' ')
print('months', end=', ') if month != 1 else print('month', end=', ')
print(f'and {days}', end=' ')
print('days', end=' ') if days != 1 else print('day', end=' ')
print(f'before all {x+2} meet for the first time')

print('\n---------------\nEnd of script')