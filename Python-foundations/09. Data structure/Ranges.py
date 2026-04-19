# Range: Sequence representing an arithmetic progression of intgers

# By default it initialized from0
a = range(3)
print(a)

for i in a:
    print(a)

# Iterating over a range
for i in range(5):
    print(i)

"""
Range signature 
1. One argument: means argument stop value
    range(stop)

2. Two arguments: means argument contains start and stop values
    range(start,stop)

3. Three arguments: means argument contains start,stop and step values
    range(start,stop,step)

* Range does not support keyword arguments
"""

# Iterating over a list
b =[3423,23423,465,786,8132,6578]
for i in b:
    print(i)


# Enumerate 
# Constructs an iterable of (index, value ) tuples around iterable object
print('Enumerate list 1: ')
l1 =[232,4456,567,879,980,1346,658]
for i in enumerate(l1):
    print(i)

# Enumerate using tuple unpacking
print('Enumerate list 1 using tuple unpacking: ')
for i,v in enumerate(l1):
    print(f"index= {i}, value= {v}")
