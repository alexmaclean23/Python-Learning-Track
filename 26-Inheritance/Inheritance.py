print()
print("####################################################")
print()

# Definition of a base class with attributes and methods
class Animal():

    def __init__(self, age, mass, legs, wings):
        self.age = age
        self.mass = mass
        self.legs = legs
        self.wings = wings

    def get_age(self):
        return self.age

    def get_mass(self):
        return self.mass

    def get_legs(self):
        return self.legs

    def get_wings(self):
        return self.wings

# Printing results of base class methods
myAnimal = Animal(age = 7, mass = 125, legs = 4, wings = 0)
print(myAnimal.get_age())
print(myAnimal.get_mass())
print(myAnimal.get_legs())
print(myAnimal.get_wings())

print()
print("####################################################")
print()

# Definition of a class that inherits the base class
class Mammal(Animal):

    def __init__(self, age, mass, legs, wings):
        self.age = age
        self.mass = mass
        self.legs = legs
        self.wings = wings
        Animal.__init__(self, self.age, self.mass, self.legs, self.wings)

# Printing results of inherited methods
myMammal = Mammal(age = 4, mass = 25, legs = 2, wings = 0)
print(myMammal.get_age())
print(myMammal.get_mass())
print(myMammal.get_legs())
print(myMammal.get_wings())

print()
print("####################################################")
print()

# Definition of a class that inherits an inherited class
class Canine(Mammal):

    def __init__(self, age, mass, legs, wings):
        self.age = age
        self.mass = mass
        self.legs = legs
        self.wings = wings
        Mammal.__init__(self, self.age, self.mass, self.legs, self.wings)

# Printing results of inherited methods
myCanine = Canine(age = 11, mass = 40, legs = 4, wings = 0)
print(myCanine.get_age())
print(myCanine.get_mass())
print(myCanine.get_legs())
print(myCanine.get_wings())

print()
print("####################################################")
print()

# Note on Abstract Classes
# An abstract class is a base class that the programmer does not intend to be instantiated.
# Instead, the class and it's methods are solely present to be inherited by its subclasses,
# and the abstract methods in that class should raise errors if called by a class instance.