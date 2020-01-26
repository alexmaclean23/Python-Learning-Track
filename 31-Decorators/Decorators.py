# Definition of an original function
def original_function():
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

# Execution of the original function
original_function()

print()
print("####################################################")
print()

# Definition of a decorator function
def decorator_function(original_function):

    def new_function():
        print("=============================================")
        original_function()
        print("=============================================")

    return new_function

# Definition of an original function with decorator tag
@decorator_function
def original_function():
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

# Execution of the decorated function
original_function()

# Note on Decorator Functions
# To toggle the decorator content and add/remove the additional code,
# simply comment out or uncomment the decorator tag with a #.