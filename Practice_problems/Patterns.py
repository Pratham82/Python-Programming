# Square
print("Square: ")
for i in range(5):
    for j in range(5):
        print("* ",end="")
    print()


# Half pyramid
print("\nHalf pyramid: ")
for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()

print("\nHalf pyramid invarsed:  ")
for i in range(5):
    for j in range(5,i,-1):
        print("*",end=" ")
    print()

print("\nHalf pyramid mirrored:")
for i in range(5):
    for j in range(i+1):
        print(" ",end=" ")
    for k in range(5,i,-1):
        print("* ",end="")
    print()

print("\nPyramid:  ")
for i in range(5):
    for j in range(5,i,-1):
        print(" ",end="")
    for k in range(-1,i,+1):
        print("* ",end=" ")
    print()

print("\nPyramid invarsed:")
for i in range(5):
    for j in range(i+1):
        print("",end=" ")
    for k in range(5,i,-1):
        print("* ",end=" ")
    print()