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