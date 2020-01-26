print()
print("####################################################")
print()

# Example of the counter module
from collections import Counter

myList = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4]
print(Counter(myList))

sentence = "this this sentence is is is iterable iterable"
words = sentence.split()
print(Counter(words))

myList = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4]
data = Counter(myList)
print(data.most_common(2))
print(sum(data.values()))

print()
print("####################################################")
print()

# Example of the defaultdict module
from collections import defaultdict

myDictionary = defaultdict(lambda: "NO VALUE")
myDictionary[0] = "zero"
myDictionary[2] = "two"
myDictionary[3] = "three"

print(myDictionary[0])
print(myDictionary[1])
print(myDictionary[2])
print(myDictionary[3])
print(myDictionary[4])

print()
print("####################################################")
print()

# Example of the ordereddict module
from collections import OrderedDict

myDictionary = OrderedDict()
myDictionary["a"] = 1
myDictionary["b"] = 2
myDictionary["c"] = 3
myDictionary["d"] = 4
myDictionary["e"] = 5

for k, v in myDictionary.items():
    print(k, v)

d1 = OrderedDict()
d1["a"] = 1
d1["b"] = 2
d2 = OrderedDict()
d2["b"] = 2
d2["a"] = 1

print(d1 == d2)

print()
print("####################################################")
print()

# Example of the namedtuple module
from collections import namedtuple

Cat = namedtuple("Cat", "name age weight")
myCat = Cat(name = "Harley", age = 14, weight = 10)

print(myCat.name)
print(myCat.age)
print(myCat.weight)

print()
print("####################################################")
print()