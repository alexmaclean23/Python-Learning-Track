# Function with *args argument
def get_sum(*args):
    return sum(args)
# Execution of *args function
print(get_sum(1))
print(get_sum(1, 2))
print(get_sum(1, 2, 3))
print(get_sum(1, 2, 3, 4))
print(get_sum(1, 2, 3, 4, 5))
print()

# Function with **kwargs argument
def get_fruit_choice(**kwargs):
    if "fruit" in kwargs:
        return "My fruit of choice is {}.".format(kwargs["fruit"])
    else:
        return "There's no fruit here."
# Execution of **kwargs argument
print(get_fruit_choice(fruit = "apple"))
print(get_fruit_choice(vegetable = "carrot"))
print(get_fruit_choice(berry = "blueberry"))
print(get_fruit_choice(fruit = "apple", vegetable = "carrot"))
print(get_fruit_choice(vegetable = "carrot", berry = "blueberry"))
print()