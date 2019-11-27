# Declaration of an integer list
myList = [1, 2, 3, 4, 5]

# Loop that does nothing using the pass keyword
for num in myList:
    pass

print()

# Loop that terminates early using the break keyword
for num in myList:
    if (num == 3):
        break
    print(num)

print()

# Loop that skips interations using the continue keyword
for num in myList:
    if (num == 3):
        continue
    print(num)