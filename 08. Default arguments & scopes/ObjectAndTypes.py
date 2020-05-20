# This function will modify the list which is passed in the function
m = [44,12,98,41,37,24,63]
def modify(k):
    k.append(99)
    print("k= ", k)

modify(m)

# Here the function does not modify the actual list we are passsing
f = [77,88,99,44,66]
def modify2(g):
    g= [11,22,33,44,55]
    print("g= ", g)

modify2(f)
print("f= ",f)

"""
Notes: 
1. Python uses named references to objects
2. id() returns a unique integer ID for an object
3. 'is' keyword determines if two names refer to the same object
4. We can test for equivalence with ==
5. Function arguments are passed by object reference, function can modify their arguments if they are mutable objects
6. type() reports the type of an object
7. dir() introspects the attributes of an object
"""