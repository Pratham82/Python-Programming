print("Top level in test.py")

def myFun():
    print("Function in  test.py")

if __name__ == "__main__":
    print("test.py is being run directly")

else:
    print("test.py is imported")

# Anthing with 0 indent block will be runs first, because there is no main mehtod
# __name__ built in variable gets assigned a string depending upon how we are running our script
#  If we run the current method directly then python will assign __main__ to it
# The if block is mainly used for code organization while working with packages. We can give the order of the functions to be called.
