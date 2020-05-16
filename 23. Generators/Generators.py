# Generator function allow us to write a function that can send back a value 
# and later resume to pick up where it left off.  
# It allows us to genrate a sequence of values over time,it uses yield statement
# When it is compiled they became object which supports and iteration protocol      

# Create cubes
def get_cubes(num):
    result =[]
    for i in range (num):
        result.append(i**3)
    return result

print(get_cubes(10))

for x in get_cubes(10):
    print(x)

# Genrators makes our program memory efficient. When we use list and returning 
# it, teh list will be loaded in memory, if the list has large amount of numbers
# then it will hoard a lot of memory. For avoiding this we can use generators

# Rather than storing the values in the list we can yield the values and later
# iterate though them for retrieval.

def get_cubes2(num):
    for i in range(num):
        yield i**3


# if we try to retrun get_cubes2() then it will provides us the genearator object
print(get_cubes2(11))

# for getting the values we have to iterate though the generator
for i in get_cubes2(11):
    print(i)