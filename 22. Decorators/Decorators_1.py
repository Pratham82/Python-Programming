# Decorater allows you to decorate a function.
# It can be used when we wanted to add new functionality to old method
# Decorators allows us to add on extra functionality to an already existing function.
# They use the @ operator and are the placed on top of the original function

def func1():
    return 2
# When we print it out we get: <function func1 at 0x0302DF58> this can be assigned to another functions
# variable func1 is actually assigned to func1() 
# and this func1 variabale can be assigned to another variable

print("func1: ",func1)


def hello():
    return "Hello there!!"

print("hello: ",hello)

greet = hello

print("greet: ",greet) # hello function objetc will be stored in greet variable

print(greet())

# hello function objetc will e stored in greet even after we delete hello function

del hello
print("After deleting")
try:
    print(hello())
except:
    print("Hello function is deleted. ")
print(greet())
