def generator_1():
    for i in range(5):
        yield i

print(generator_1)
g = generator_1()

# next() method will print the next value 
# Generator object will calls this method internally.

print(next((g)))
print(next((g)))
print(next((g)))
print(next((g)))
print(next((g)))

# If we try to print the next object beyond the range then we will get an error 
# In for loop it automatically catches the (StopIteration)error and stop 
# the next element from printing

