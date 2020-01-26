# Definition of a function that creates a list of cubes
def get_cubes(max):
    cubes = []
    for num in range(max):
        cubes.append(num ** 3)
    return cubes

# Printing first 10 values of the function
for x in get_cubes(10):
    print(x)

print()
print("####################################################")
print()

# Definition of a generator function
def get_cubes(max):
    for num in range(max):
        yield num ** 3

# Iterating through the generator function
for num in get_cubes(10):
    print(num)

# Sequencing outputs of the generator function
print()
item = get_cubes(10)
print(next(item))
print(next(item))
print(next(item))
print(next(item))
print(next(item))
print(next(item))
print(next(item))
print(next(item))
print(next(item))
print(next(item))

print()
print("####################################################")
print()

# Modifying a String to make it a generator
str = "Hello"
generatorStr = iter(str)

# Sequencing the String like a generator
print(next(generatorStr))
print(next(generatorStr))
print(next(generatorStr))
print(next(generatorStr))
print(next(generatorStr))