# Demonstration of nested conditionals
myNum = int(input("Input a number: "))
if (myNum > 0):
    myNum += 1
    if (myNum > 2):
        myNum -= 2
    elif (myNum == 2):
        myNum /= 2
    else:
        myNum += 1
else:
    myNum *= 4
print(myNum)
print()

# Demonstration of nested loops
myNum = int(input("Input a number: "))
for x in range(1, 1001):
    myNum -= 1
    for y in range(1, 6):
        myNum += 1
print(myNum)
print()

# Demonstration of nested loops and conditionals
myNum = int(input("Input a number: "))
while (myNum <= 10000):
    myNum += 1
    if (myNum == 5000):
        print(myNum)
        break
else:
    print("myNum is > 10,000")
print()