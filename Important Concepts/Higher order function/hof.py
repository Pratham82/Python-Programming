# A function is called Higher Order Function if it contains other functions as
#  a parameter or returns a function as an output i.e, the functions that 
# operate with another function are known as Higher order Functions. 


def parent_fn(inner_fn,arg):
    return inner_fn(arg)

add_10 = lambda n: print(n +10)

parent_fn(add_10, 20)