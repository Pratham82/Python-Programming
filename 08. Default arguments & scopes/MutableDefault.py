def Add_spam(menu=[]):
    menu.append("spam")
    print (menu)

l1 = ['red','blue','green']

# Here the add_spam method is called and "spam" is appended to the list entered 
Add_spam(l1)

# If we don't provide any list it automatically adds spam to the newly created list
Add_spam()
Add_spam()
Add_spam()

# Always use immutable objects for default values

# The None keyword is used to define a null variable or an object. 
# In Python, None keyword is an object, and it is a data type of the class NoneType.
def Add_spam(menu=None):
    if menu is None:
        menu =[]
    menu.append("spam")
    print (menu)

Add_spam()
Add_spam()
Add_spam()
