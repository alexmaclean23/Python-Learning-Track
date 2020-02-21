# Declaration of an empty set
mySet = set()
print(mySet)
print()

# Adding items to a set
print(mySet)
mySet.add(0)
print(mySet)
mySet.add(1)
print(mySet)
mySet.add(1)
print(mySet)
print()

# Removing items from a set
print(mySet)
mySet.discard(0)
print(mySet)
print()

# Removing all items from a set
print(mySet)
mySet.clear()
print(mySet)
print()

# Casting lists to sets
myList = [1, 1, 1, 2, 2, 3]
print(myList)
mySet = set(myList)
print(mySet)
print()

# Casting Strings to sets
myString = "Mississippi"
print(myString)
mySet = set(myString)
print(mySet)
print()