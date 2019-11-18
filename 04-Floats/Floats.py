# Declaration of a few floats
x = 7.0
y = 21.0
z = 45.0

# Basic math operations using floats
addInt = x + z
subtractInt = z - y
multiplyInt = x * y
divideInt = y / x
modInt = z % x
powerInt = y ** z
everythingInt = (y ** 7) / ((z + y) - (-(y * x)))

# Printing of the math calculations
print(addInt)
print(subtractInt)
print(multiplyInt)
print(divideInt)
print(modInt)
print(powerInt)
print(everythingInt)
print()

# Demonstration of decimal accuracy
result = 444 / 777
print(result)
# Formats variable with width of 1 and accuracy of 3 decimal places
print("The rounded result is{r: 1.3f}".format(r = result))