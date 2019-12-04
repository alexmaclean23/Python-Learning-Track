# Definition of a funciton that returns the square of the input
def square_num(num):
    return num**2

# Declaration of a list of numbers to be fed into the function
myNums = [1, 2, 3, 4, 5]

# Use of the map function to iterate the function through the list and print results
for number in map(square_num, myNums):
    print(number)

# Use of the map function to iterate the function through the list and create a new list
print()
myNewNums = list(map(square_num, myNums))
print(myNewNums)

print()

# Definition of a function that checks if a number is even
def is_even(num):
    if ((num % 2) == 0):
        return True
    else:
        return False

# Declaration of a list of numbers to be fed into the function
myNums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use of the filter function to iterate the function through the list and print results
for number in filter(is_even, myNums):
    print(number)

# Use of the filter function to iterate the function through the list and create a new list
print()
myNewNums = list(filter(is_even, myNums))
print(myNewNums)

print()
print("####################################################")
print()

# Replacement of the initial function with a lambda expression
myNums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(map(lambda num:num**2, myNums)))
print(list(filter(lambda num:num%2==0, myNums)))