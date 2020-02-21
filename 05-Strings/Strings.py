# Declaration of a String
print("Hello world!")
# Declaration of a few Strings with escape sequences
print("Hello\tworld!")
print("Hello\nworld!")
print()

# Redeclaration of a String
exampleString = "The quick, brown fox jumped over the lazy dog."
print(exampleString)
# Demonstration of the implicit length method
print('The length of the string above is', len(exampleString), 'characters.')
print()

# Printing out of individual characters of a String
print(exampleString[17])
print(exampleString[18])
print(exampleString[19])
print(exampleString[-1])
print()

# Printing out a splice from the middle of a String
print(exampleString[17: 20: 1])
print()

# Redeclaration of a String
exampleString = "abcdefghijklmnopqrstuvwxyz"
# Printing out of various segments of a String
print(exampleString[::])
print(exampleString[:3])
print(exampleString[-3:])
print(exampleString[::3])
print(exampleString[::-1])
print()

# Redeclaration of a String
exampleString = "Hello"
print(exampleString)
# Demonstration of a String modification
exampleString = exampleString[1:]
print("Y" + exampleString + "w")
print()

# Redeclaration of a String
exampleString = "Hi"
print(exampleString)
# Example of String addition
exampleString = exampleString + exampleString
print(exampleString)
exampleString = "Hi"
# Example of String multiplication
exampleString = exampleString * 10
print(exampleString)
print()

# Redeclaration of a String
exampleString = "The quick brown fox jumped over the lazy dog"
# Demonstration of .format method
exampleString = "The {1} {2} {0} jumped over the {l} {d}".format('fox', 'quick', 'brown', l = 'lazy', d = 'dog')
print(exampleString)
print()

# Redeclaration of a String
exampleString = "The quick brown fox jumped over the lazy dog"
# Demonstration of an fString
animal1 = "fox"
animal2 = "dog"
exampleString = f"The quick brown {animal1} jumped over the lazy {animal2}"
print(exampleString)