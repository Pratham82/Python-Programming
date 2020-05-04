'''
n Python, we can pass a variable number of arguments to a function using special symbols. There are two special symbols:
*args (Non Keyword Arguments)
**kwargs (Keyword Arguments)
We use *args and **kwargs as an argument when we are unsure about the number of arguments to pass in the functions.
'''

def func(a,b,c,d):
    return sum((a,b,c,d))*0.18

print(func(12,14,45,12))

# when we don't know th number of arguments that user is going to enter then we use
# args there it allows us to set an arbitrary amount of arguments
# all the variables will be inserted into the tuple and the action will be performed on the tuple as a whole

def func1(*args):
    return sum(args) * 0.18

print(func1(2323,344,534,6,7,567867,878,989,980,980))


def func1(*args):
    for i in args:
        print(i)

print(func1(2323,344,534,6,7,567867,878,989,980,980))

# kwargs  allows us to add a keyword argument
# kwargs returns back a dictionary

def func3(**kwargs):
    if 'fruit' in kwargs:
        print(f"My fruit of choice is {kwargs['fruit']}")
    else:
        print("I did not found any fruits")


print(func3(fruit="apple",car="aston martin",color="red",band="maroon 5"))

# Wec can use different words for args and kwargs. But args and kwargs are prefred as per the convention.

# Combination of both args and kwargs 

def combo(*args,**kwargs):
    print(args)      # List
    print(kwargs)    # Dictionary
    print(f"These are best combinations {args[0]},{kwargs['food']}")
    
print(combo(87,4,5,food='apple',color='red',watch='casio'))