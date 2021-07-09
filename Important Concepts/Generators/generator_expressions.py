names_list = [
    'Adam', 'Anne', 'Barry', 'Brianne', 'Charlie', 'Cassandra', 'David', 'Dana'
]

uppercase_names = (name.upper() for name in names_list)
# This will return a generator object
print(uppercase_names)

# For accessing this generator object we will use list on in
print(list(uppercase_names))


def new_gen(n):
    for i in range(n):
        if i % 2 == 0:
            yield i


val = new_gen(10)
print(next(val))  # prints 0
print(next(val))  # prints 2
print(next(val))  # prints 4
print(next(val))  # prints 6
print(next(val))  # prints 8
# print(next(val))  # returns error because the list is exhausted
# It willl only returns next value until the list has them, once list is finished it will return an error

# Generator object can also be called in used in a place of an iterable such as list

# This for loop will not print anything becuase the values are already exhausted before
# But here we will not get any error because python internally hanles the errore
for i in val:
    print(i)

# For using the values again, we have to store the generator values in the new variable
print('---')
val2 = new_gen(10)
for i in val2:
    print(i)

# Instead creating a new generator function storing it in another varaible and printing it in a for loop we can diretly make a call to generator function itself
print('---')
for i in new_gen(10):
    print(i)

# Or we can pass the generator expression as well
print('---')
for i in (i for i in range(10) if i % 2 == 0):
    print(i)

# Notes
"""
    Generator objects:
    1. cannot be reused
    2. Calling next on an exhausted generator raises Stopiteration exception
    3. The for loop handles Stopiteration
"""
"""
### Challenge
Create a fibonacci sequence using generators
"""
# Creating fibonacci in normal way
print('==')
start, start1 = 0, 1
next = 0
for i in range(10):
    next = start1 + start
    start = start1
    start1 = next
    print(next)

# Cleaner fibonacci
# initializing starting values
first, second, fib_list = 0, 1, []
for i in range(10):
    # First sum the starting values and appending them to our list
    fib_list.append(second)
    # Reassing the variables
    # Here the first variable will get the value of second and the second will get the value of first + second
    first, second = second, first + second
print(fib_list)


# Using python generator
def fib_gen(n):
    first, second = 0, 1
    for _ in range(n):
        yield second
        first, second = second, first + second


print('fibonacci using generators')
print(fib_gen(10))  # Returns generator object
for i in fib_gen(10):
    print(i)
