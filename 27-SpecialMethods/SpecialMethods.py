# Definition of a class with no special methods
class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

# Printing out features of the class
myBook = Book(title = "1984", author = "George Orwell", pages = 200)
print(myBook)

print()
print("####################################################")
print()

# Definition of a class with special methods
class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} is a book by {self.author}"

    def __len__(self):
        return self.pages

# Printing out features of the class
myBook = Book(title = "1984", author = "George Orwell", pages = 200)
print(myBook)
print(len(myBook))

# Note on __name__ and "__main__"
# Larger scripts, particularly modules, often end with a block of code inside of an if statement.
# Because python automatically sets the default __name__ variable to "__main__" when a script is run,
# the 'if __name__ == "__main__": block only executes if the module is run as the primary script, not
# an add-on. The block of code below can run whatever functions are necessary, but the idea as a whole
# is simply to give the script the ability to check if it is being run independently, so it can adjust
# accordingly.