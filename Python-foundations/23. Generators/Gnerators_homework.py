# Problem 1
# Create a generator that generates the squares of numbers up to some number N.
def squares_gen(num):
    for i in range(num):
        yield i**2

print(squares_gen)
# Iterating through generator
for i in squares_gen(10):
    print(i)

# Problem 2
# Create a generator that yields "n" random numbers between a low and high number (that are inputs).
import random 

def random_gen(start,end,num):
    for i in range(num):
         i = random.randint(start,end)
         yield i

print(random_gen)
# Iterating through generator
for i in random_gen(1,10,10):
    print(i)

# Problem 3
# Use the iter() function to convert the string below into an iterator:

# Problem 3
# Use the iter() function to convert the string below into an iterator:

string1 = "Example_string"
string1_iterator =iter(string1)

for i in string1_iterator:
    print(i)

# Problem 4
# Explain a use case for a generator using a yield statement where you would not want to use a normal function with a return statement.
# Ans- We can use it when the data that we are storing is extremely huge 
# In that case we can use yield keyword retrieving values one by one, rather than
# storing it in a list

# Extra credit
# gencomp

list1 = [213,4,235,43,56,546,5]
list_comp =  [ i for i in list1 if i>200]
print(list_comp)

gen_comp =(i for i in list1 if i>200)
print("gen_comp object: ",gen_comp)
# iterating thorugh generator
for i in gen_comp:
    print (i)

