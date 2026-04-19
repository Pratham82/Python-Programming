# Passing function as an argument 

def greeting():
    return 'Welcome user!!'

def temp(any_func):
    print("temp function code running now")
    print(greeting())

temp(greeting)


# Manipulating other function variables

def entry(name="def name"):
    return f"Hi there {name}, welcome to python"

def mid(fun, new_name='def name 2'):
    print("Middleware running")
    print(fun(new_name))
    print("Process is finished")

mid(entry)