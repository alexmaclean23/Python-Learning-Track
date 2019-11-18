# Declaration of a few lists
myInts = [1, 2, 3, 4]
myFloats = [1.0, 2.0, 3.0, 4.0]
myStrings = ["Hi", "Hey", "Hello", "Howdy"]
myBooleans = [True, False, True, False]
myDataTypes = [7, 23.0, "Greetings", True]

# Printing of the lists
print(myInts)
print(myFloats)
print(myStrings)
print(myBooleans)
print(myDataTypes)
print()

# Printing of the length of a list
length = len(myDataTypes)
print(length)
print()

# Printing of individual items in a list
print(myDataTypes[0])
print(myDataTypes[1])
print(myDataTypes[2])
print(myDataTypes[3])
print()

# Printing of selected items in a list
print(myDataTypes[1:3])
print()

# Addition of lists
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
newList = list1 + list2
print(newList)
print()

# Modification of lists
numList = ["one", "two", "three", "four"]
print(numList)
numList[1] = "TWO"
print(numList)
numList[3] = 4
print(numList)
print()

# Appending values onto a list
numList = ["one", "two", "three", "four"]
print(numList)
numList.append("five")
print(numList)
print()

# Popping values off of a list
numList = ["one", "two", "three", "four"]
print(numList)
numList.pop(3)
print(numList)
print()

# Sorting items in a list
list1 = [5, 2, 4, 1, 3]
list2 = ['a', 'd', 'b', 'e', 'c']
print(list1)
print(list2)
list1.sort()
list2.sort()
print(list1)
print(list2)
print()

# Reversing items in a list
numList = [1, 2, 3, 4, 5]
print(numList)
numList.reverse()
print(numList)