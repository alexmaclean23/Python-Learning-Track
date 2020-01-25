print()
print("####################################################")
print()

# Definition of a class that does nothing
class MyClass():

    pass

# Printing out type of variable set to the object
myVar = MyClass()
print(type(myVar))

print()
print("####################################################")
print()

# Definition of a class with a constructor and attributes
class MyDog():

    def __init__(self, age, breed, name):
        self.age = age
        self.breed = breed
        self.name = name

# Printing out attribute of the object
myVar = MyDog(age = 9, breed = "King Charles", name = "Finn")
print(myVar.name)

print()
print("####################################################")
print()

# Definition of a class with a contructor, attributes, and methods
class MyCat():

    family = "feline"

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def print_age(self):
        return self.age

    def print_name(self):
        return self.name

# Printing out result of method of the object
myVar = MyCat(age = 14, name = "Harley")
print(myVar.print_name())

print()
print("####################################################")
print()