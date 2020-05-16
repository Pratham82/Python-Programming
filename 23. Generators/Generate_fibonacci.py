# Generator function
def fib_sq(n):
    a,b = 1,1
    for i in range(n):
        yield a 
        a, b = b, a+b

print(fib_sq(10))
for i in fib_sq(10):
    print(i)


# Normal funcion
# This function takes more memory space than generators.
def fib_sq(n):
    a,b = 1,1
    fib =[]
    for i in range(n):
        fib.append(a)
        a, b = b, a+b
    return fib
print(fib_sq(10))