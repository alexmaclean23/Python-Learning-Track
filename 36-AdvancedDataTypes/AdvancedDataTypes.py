print()
print("####################################################")
print()

# Advanced Numbers

# Declaration of an integer and a float
myInt = 128
myFloat = 39.877

# Converting integers to hexadecimal and binary
myBin = bin(myInt)
print(myBin)
myHex = hex(myInt)
print(myHex)
print()

# Rounding floats to a specified number of digits
myRnd = round(myFloat, 0)
print(myRnd)
myRnd = round(myFloat, 1)
print(myRnd)
myRnd = round(myFloat, 2)
print(myRnd)
print()

# Using built-in number functions
myPow = pow(2, 3)
print(myPow)
myAbs = abs(-2)
print(myAbs)

print()
print("####################################################")
print()

# Advanced Strings

# Declaration of a string
myString = "hello world"

# Capitalizing the first letter of a String
newString = myString.capitalize()
print(newString)
print()

# Converting an entire String to uppercase
newString = myString.upper()
print(newString)
print()

# Converting an entire String to lowercase
newString = myString.lower()
print(newString)
print()

# Count the occurences of a character in a String
oCount = myString.count('o')
print(oCount)
print()

# Index the first position of a character in a String
oFind = myString.find('o')
print(oFind)
print()

# Center the String between characters of a certain length
newString = myString.center(30, '*')
print(newString)
print()

# Check if all characters in a String are alphabetical / numeric / alphanumeric
newString = "Hello"
isAlphabetical = newString.isalpha()
print(isAlphabetical)
isNumeric = newString.isnumeric()
print(isNumeric)
isAlphanumeric = newString.isalnum()
print(isAlphanumeric)
print()

# Check if all characters in String are uppercase / lowercase / spaces
newString = "hello"
isUpper = newString.isupper()
print(isUpper)
isLower = newString.islower()
print(isLower)
isSpace = newString.isspace()
print(isSpace)
print()

# Check if a String ends with a specific character
endsO = myString.endswith('o')
print(endsO)
endsD = myString.endswith('d')
print(endsD)
print()

# Split a String at a certain character and return list (exclude character)
myList = myString.split(' ')
print(myList)
print()

# Split a String at a certain character and return list (include character)
myList = myString.partition(' ')
print(myList)

print()
print("####################################################")
print()