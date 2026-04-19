# Arguments with default values must come after those with default values
# This method takes message as an input and the length of the message is getting multiplied by the border 
# Here border is default variable so even if it is not passed while method call it takes default border value as '-'
#  We can change this value while calling the method

def banner(message, border='-'):
    # Here message is positional argument and border is key argument
    line= border * len(message)
    print(line)
    print(message)
    print(line)

m1 = (input("Enter message: "))
b1 = (input("Enter border: "))
banner(m1,b1)

m2 =  (input("Enter message: "))
b2 = (input("Enter border: "))
banner(m2,b2)

# def i statement executed at runtime
# default arguments are evaluated when def is executed
# immutable default values don't cause problems
# mutable default values can cause problems

