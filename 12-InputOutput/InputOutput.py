# Declaration and opening of a file
myFile = open("Python-Learning-Track/12-InputOutput/sampleFile.txt")

# Reading the contents of a file as a String
myFile.seek(0)
print(myFile.read())
print()

# Reading the contents of a file as a List
myFile.seek(0)
print(myFile.readlines())
print()

# Closing file at end of use <IMPORTANT>
myFile.close()

# Using a file temporarily in a function with read permissions
with open("Python-Learning-Track/12-InputOutput/sampleFile.txt", mode = "r") as myFile:
    fileContents = myFile.read()
print(fileContents)
print()

# Using a file temporarily in a function with append permissions
with open("Python-Learning-Track/12-InputOutput/sampleFile.txt", mode = "a") as myFile:
    myFile.write("\nThis is a .txt file.")

# Using a file temporarily in a function with read permissions
with open("Python-Learning-Track/12-InputOutput/sampleFile.txt", mode = "r") as myFile:
    fileContents = myFile.read()
print(fileContents)
print()

# Using a file temporarily in a function with write permissions
with open("Python-Learning-Track/12-InputOutput/sampleFile.txt", mode = "w") as myFile:
    myFile.write("This is a .txt file.\nThis is a .txt file.\nThis is a .txt file.")

# Using a file temporarily in a function with read permissions
with open("Python-Learning-Track/12-InputOutput/sampleFile.txt", mode = "r") as myFile:
    fileContents = myFile.read()
print(fileContents)
print()

# The mode identifier "r+" allows a file to be read, and then written
# The mode identifier "w+" allows a file to be written, and then read