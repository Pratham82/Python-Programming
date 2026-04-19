# returning function inside a function
def hello(name="Kirk"):
    print("This is start fo hello function")

    # greet and welcome has limited scope of hello function
    def greet():
        return "\t This is greet() method inside hello function"
    def welcome():
        return "\t This is welcome() method inside hello function"
    
    # print(greet())
    # print(welcome())
    # print("This is end of hello function")

    print("returning a function")
    if name == 'Kirk':
        return greet
    else:
        return welcome

# greet function object was assigned to fun_new, because condition satisfied
fun_new = hello("Kirk") 
print(fun_new)     # <function hello.<locals>.greet at 0x00C512B0>