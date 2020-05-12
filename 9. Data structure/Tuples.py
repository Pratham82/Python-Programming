# Tuples: are immutable set of arbitary objects.

# Declaring tuples:

a =(1,34543,6756,"test","pretext",'w',123,34534)

# Nested tuples:

b =((231,123),("Test1",3443),(7889,"Test2",'r'),(2434,"Operate"))

# Length fo tuple:

print("Length of tuple a: ",len(a),"\n")

# Getting objects by its index value

print("\nObjects on index 3: ",a[3])
print("\nObjects on index 3(2): ",b[3][1])

# Iterating though a tuple
print("\nIterating though a tuple a:")
for i in a:
    print(i)

print("\nIterating though a tuple b:")
for i in b:
    print(i)

# Creating tuples with 1 element
c= ("Obj1",)
print("Tuple c: ",c)

# Creating empty tuple
d= ()
print("Tuple d: ",d)

# Swapping in tuples
a1 = "test1"
b1 = "test2"
print("a1: ",a1)
print("b1: ",b1)
a1,b1 =b1,a1
print("After swapping: ")
print("a1: ",a1)
print("b1: ",b1)






