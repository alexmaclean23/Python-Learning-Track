print()
print("####################################################")
print()

# Advanced Lists

# Declaration of a list
myList = [1, 1, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5]

# Counting occurences of an item in a list
number4 = myList.count(4)
print(number4)
print()

# Appending a list to another list
myList.extend([6, 6, 6])
print(myList)
print()

# Indexing the first occurence of an item in a list
location5 = myList.index(5)
print(location5)
print()

# Insert element into specific index in list
myList.insert(6, "placeholder")
print(myList)
print()

# Remove first occurence of element from list
myList.remove("placeholder")
print(myList)

print()
print("####################################################")
print()

# Advanced Dictionaries

# Creating a dictionary using an embedded statement
myDictionary = {x: x**2 for x in range(10)}
print(myDictionary)
print()

# Return keys from dictionary individually
for x in myDictionary.keys():
    print(x)
print()

# Return values from dictionary individually
for x in myDictionary.values():
    print(x)
print()

# Return items from dictionary individually
for x in myDictionary.items():
    print(x)
print()

print()
print("####################################################")
print()

# Advanced Sets

# Declaration of a set
mySet = set()
mySet.add(1)
mySet.add(2)
mySet.add(3)
print(mySet)
print()

# Copying a set
newSet = mySet.copy()
print(newSet)
print()

# Returning difference between two sets
newSet.add(4)
print(mySet)
print(newSet)
myDifference = mySet.symmetric_difference(newSet)
print(myDifference)
print()

# Returning intersection between two sets
mySet.add(5)
print(mySet)
print(newSet)
myIntersection = newSet.intersection(mySet)
print(myIntersection)
print()

# Checking if two sets have no intersection
s1 = {1, 2, 3}
s2 = {4, 5, 6}
isDisjointed = s1.isdisjoint(s2)
print(isDisjointed)
print()

# Checking if a set contains all values of a smaller set
largeSet = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
smallSet = {0, 2, 4, 6, 8}
isSuperset = largeSet.issuperset(smallSet)
print(isSuperset)
isSubset = smallSet.issubset(largeSet)
print(isSubset)
print()

# Create a new set with all values of other sets
s3 = s1.union(s2)
print(s3)

print()
print("####################################################")
print()