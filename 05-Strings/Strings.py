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

# Default methods for Strings:
x = ""
    # x.capitalize
    # x.casefold
    # x.center
    # x.count
    # x.encode
    # x.endswith
    # x.expandtabs
    # x.find
    # x.format
    # x.format_map
    # x.index
    # x.isalnum
    # x.isalpha
    # x.isascii
    # x.isdecimal
    # x.isdigit
    # x.isidentifier
    # x.islower
    # x.isnumeric
    # x.isprintable
    # x.isspace
    # x.istitle
    # x.isupper
    # x.join
    # x.ljust
    # x.lower
    # x.lstrip
    # x.maketrans
    # x.mro
    # x.partition
    # x.replace
    # x.rfind
    # x.rindex
    # x.rjust
    # x.rpartition
    # x.rsplit
    # x.rstrip
    # x.split
    # x.splitlines
    # x.startswith
    # x.strip
    # x.swapcase
    # x.title
    # x.translate
    # x.upper
    # x.zfill
    # x.__add__
    # x.__base__
    # x.__class__
    # x.__contains__
    # x.__delattr__
    # x.__dict__
    # x.__dir__
    # x.__eq__
    # x.__format__
    # x.__ge__
    # x.__getattribute__
    # x.__getitem__
    # x.__getnewargs__
    # x.__gt__
    # x.__hash__
    # x.__init__
    # x.__init_subclass__
    # x.__iter__
    # x.__le__
    # x.__len__
    # x.__lt__
    # x.__mod__
    # x.__mul__
    # x.__ne__
    # x.__reduce__
    # x.__reduce_ex__
    # x.__repr__
    # x.__rmod__
    # x.__rmul__
    # x.__setattr__
    # x.__sizeof__
    # x.__str__
    # x.__subclasshook__
    # x.__weakref__