'''
Opening and dealing with files
textFiles
'''

# Opens "Christmas_song.txt" in writable mode
# If the file doesn't exist, it is created

print("Opening Christmas_song.txt")
songLyric = open("Christmas_song.txt","w")

# File methods and properties that are available
print("File methods and properties:")

# The name property provides the file system name of the associated file
print("name: ", songLyric.name)

# The mode property provides details on which mode the file
print("mode: ", songLyric.mode)

# The closed property returns true if the file is closed
# The readable() method returns true if the file is readable
# The writable() method returns true if the file is writable
print("The file is Closed") if songLyric.closed else print('File isn not Closed')
print("The file is Readable") if songLyric.readable() else print('File is not Readable')
print("The file is Writable") if songLyric.writable() else print('File is not Writable')

# Closes the file to release the resources
songLyric.close