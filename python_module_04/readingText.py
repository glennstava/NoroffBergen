# The file is opened using the readable mode

speach = open("Gettysburg_address.txt","r")

# Display all the contents of the file
print(speach.read())

print('\n----\n')
print(f"Position {speach.tell()}")
print("Resetting position to 122")
speach.seek(122)
print('\n----\n')

# Display 20 lines of the text all the contents of the file again
count = 1
for line in speach:
    if count == 20:
        break
    
    # As there is an extra newline character at the end of each line
    print(count, end=' - ')
    print(line, end='')
    count += 1

speach.close()