verdier = [11,43,54,32,67,54,34,67,78]
sluttsum = sum(verdier)
snitt = int(sluttsum / len(verdier))

print(sluttsum)
print(snitt)

totalsum = 0
for x in verdier:
    totalsum += x
    
print(totalsum)