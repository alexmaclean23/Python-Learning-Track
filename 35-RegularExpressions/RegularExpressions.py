# Import regular expressions library
import re

print()
print("####################################################")
print()

# Example of search method in regular expressions
searchWord = "Hello"
searchPhrase = "Hello World!"
if (re.search(searchWord, searchPhrase)):
    print("Match found.")
else:
    print("No match found")
print()

# Indexing search method's match
match = re.search("lmnop","abcdefghijklmnopqrstuvwxyz")
print(match.start())
print(match.end())

print()
print("####################################################")
print()

# Example of split function in regular expressions
splitChar = "#"
splitPhrase = "abcdefghijklm#nopqrstuvwxyz"
splitList = re.split(splitChar, splitPhrase)
print(splitList)

print()
print("####################################################")
print()

# Example of findall method in regular expressions
searchWord = "one"
searchPhrase = "one one one two two three two two one one one"
searchList = re.findall(searchWord, searchPhrase)
print(searchList)

print()
print("####################################################")
print()

# Regular Expression Syntax
# The regular expressions library has a set of specific syntax rules associated
# with it. This syntax is used to demonstrate the number of times a following
# character follows a lead character. For the example below, the lead character
# is '1' and the following character is 'a'.
#
# 1a* refers to anytime a '1' is followed by zero or more instances of 'a'
# 1a+ refers to anytime a '1' is followed by one or more instances of 'a'
# 1a? refers to anytime a '1' is followed by exactly zero or one instances of 'a'
# 1a{n} refers to anytime a '1' is followed by exactly 'n' instances of 'a'
# 1a{x, y} refers to anytime a '1' is followed by the exact range of 'x' to 'y' instances of 'a'
#
# Examples:
# 1a*             |    1 ... 1a ... 1aa ... 1aaa ... 1aaaa ... 1aaaaa ... (etc)
# 1a+             |    1a ... 1aa ... 1aaa ... 1aaaa ... 1aaaaa ... 1aaaaaa ... (etc)
# 1a?             |    1 ... 1a
# 1a{5}           |    1aaaaa
# 1a{2, 5}        |    1aa ... 1aaa ... 1aaaa