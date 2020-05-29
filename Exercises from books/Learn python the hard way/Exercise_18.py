#  Names functions and varibales

def print_args(*args):
    a1,a2 = args
    print("args provided: ", a1,a2)

def print_two(arg1,arg2):
    print("argument 1: ", arg1, 'argument 2: ', arg2)

def print_one(one):
    print("One argument: ",one)

def printNone():
    print("No arguments provided")

print_args(23,12)
print_two(3434,435)
print_one(24242)
printNone()

