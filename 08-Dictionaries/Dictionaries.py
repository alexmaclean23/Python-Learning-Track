# Declaration of a couple dictionaries
myInts = {"one": 1, "two": 2, "three": 3, "four": 4}
myFloats = {"one": 1.0, "two": 2.0, "three": 3.0, "four": 4.0}
myStrings = {"one": "One", "two": "Two", "three": "Three", "four": "Four"}
myBooleans = {"one": True, "two": False, "three": True, "four": False}
myDataTypes = {"integer": 1, "float": 1.0, "String": "one", "Boolean": True}

# Printing out of the dictionaries
print(myInts)
print(myFloats)
print(myStrings)
print(myBooleans)
print(myDataTypes)
print()

# Printing out of individual dictionary items
print(myDataTypes["integer"])
print(myDataTypes["float"])
print(myDataTypes["String"])
print(myDataTypes["Boolean"])
print()

# Modifying items in a dictionary
print(myDataTypes)
myDataTypes["Boolean"] = False
print(myDataTypes)
print()

# Appending items to a dictionary
print(myDataTypes)
myDataTypes["null"] = None
print(myDataTypes)
print()

# Extracting keys, values, and items from a dictionary
keys = myDataTypes.keys()
values = myDataTypes.values()
items = myDataTypes.items()
print(keys)
print(values)
print(items)
print()