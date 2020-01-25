# Definition of function that adds parameters
def add_numbers(number1, number2):
    return number1 + number2

# Definition of function that asks for input numbers, and catches errors for faulty input types
def get_numbers():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
    except:
        print("Please enter a number!")
    else:
        result = add_numbers(num1, num2)
        print(result)
    finally:
        print()
        get_numbers()

# Running method
get_numbers()

# Note on Individual Exceptions
# In addition to executing the general exception block, specific exceptions can be
# caught by individual blocks, accomplished by placing the name of the exception
# before the colon.