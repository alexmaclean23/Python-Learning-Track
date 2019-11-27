# Declaration of various data types
myList = [1, 2, 3, 4, 5]
myString = "Hello"

# For loop to print integers in list
for integers in myList:
    print(integers)

print()

# For loop to print letters in String
for letters in myString:
    print(letters)

print()

# For loop to print dash for each integer in list
for integers in myList:
    print("-")

print()

# For loop to tally letters in String
numLetters = 0
for letters in myString:
    numLetters += 1
print(numLetters)