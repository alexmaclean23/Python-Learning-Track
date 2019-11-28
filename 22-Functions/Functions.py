# Simple print function
def hello_world():
    print("Hello World!")
# Execution of print function
hello_world()
print()

# Simple print function with docs
def hello_world():
    '''
    DOCSTRING: A function that prints "Hello World!"
    INPUT: None
    OUTPUT: String
    '''
    print("Hello World!")
# Execution of print function
hello_world()
print()

# Simple print function with argument
name = input("What is your name? ")
def greetings(name):
    print(f"Hello {name}!")
# Execution of print function
greetings(name)
print()

# Simple return function with argument
name = input("What is your name? ")
def greetings(name):
    return f"Hello {name}!"
# Execution of return function
print(greetings(name))
print()

# Simple return function with arguments
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
def add_function(num1, num2):
    return num1 + num2
# Execution of return function
print(add_function(num1, num2))
print()

# Simple return function with arguments
hasWord = False
word = input("Input a word to check for: ")
sentence = input("Input a sentence to search: ")
def word_in_sentence(word, sentence):
    if word.lower() in sentence.lower():
        hasWord = True
    else:
        hasWord = False
    return hasWord
# Execution of return function
print(word_in_sentence(word, sentence))
print()

# Example: Pig Latin generator
sentence = input("Enter a sentence to convert to Pig Latin: ")
def convert_sentence(sentence):
    pigLatin = ""
    words = sentence.split()
    for word in words:
        if word[0] == 'a':
            word = word + "ay"
            pigLatin += (word + " ")
        elif word[0] == 'e':
            word = word + "ay"
            pigLatin += (word + " ")
        elif word[0] == 'i':
            word = word + "ay"
            pigLatin += (word + " ")
        elif word[0] == 'o':
            word = word + "ay"
            pigLatin += (word + " ")
        elif word[0] == 'u':
            word = word + "ay"
            pigLatin += (word + " ")
        else:
            word = word[1:] + word[0] + "ay"
            pigLatin += (word + " ")
    return pigLatin    
# Execution of the Pig Latin function
print(convert_sentence(sentence))
print()