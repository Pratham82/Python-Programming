class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __len__(self):
        return self.pages

    # String representation
    def __str__(self):
        return f"Book: {self.title}, Author: {self.author}, Pages: {self.pages}"
    
    # Special method for delete
    # The following method with do the things which are mentioned when the object is delted
    def __del__(self):
        print("Book object is deleted")

book1 = Book("Think and grow rich", "napoleon Hill", 200)

# Here we can see, that predefined methods can be used on th list1
list1 = [34,345,345345,53]
print(len(list1))

# But the same len method won't work with our predefined class object 
# For using that we can define special method in our class using __len__
# __len__ or any methods are called special methods or dunder methods.
print(len(book1))

# When we are using print method with our object it normally returns a string representation
# but with the book1 object which is an object of user defined it will only give the object's memory location for getting actual string representation we have to use __str__ method in class Book
print(book1)

# Delting a variabale
del book1
