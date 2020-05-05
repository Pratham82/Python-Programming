def square(n):
    print("Square of number: ", n*n)
square(3)

list1=[11,12,13]

# Using map to pass functions with iterables
# Iterating through the list
for  i in map(square,list1):
    print(i)

# Storing the map in list
list_new= list(map(square,list1))

# Splicer
def splicer(string):
    if len(string) %2==0:
        return "Even"
    else:
        return string[0] 

print(splicer("Hello"))

words =["Hi","Its","an", "amazing","day"]

# Combining lists with methods with the use of map

print(list(map(splicer,words)))

# Filter function 
# The filter() method filters the given iterable with the help of a function that tests each element in the iterable to be true or not.

def EvenChecker(n):
    return n%2 == 0

nums =[1,2,3,4,5,6,7,8]

print(list(filter(EvenChecker,nums)))

# How to convert your function to lambda expression

# Simplifying this: 
'''
Simplifying 1

def square_2(n):
    result = n*n
    return result

Simplifying 2

def square_2(n): return n**2

lambda expression: it is also known as anonymous function because the functionality that you only intnet to use once.
Thats why we don't give it a name. Also we don't use the def keyword and replace that with the lambda keyword
'''
# Finally converting to lambda expression
square_2= lambda n: n**2
print(square_2(12))

nums =[10,20,30,40,50,60,70,80]
nums2=[45,21,45,99,74,12,73]
# Combining lambda and map
print(list(map(lambda num:num**2,nums)))

# Combining lambda and filter
print(list(filter(lambda n:n%2==0,nums2)))

# lambda function for getting the 1st character of a string
print(list(map(lambda c: c[0],words)))

# Lambda function for reversing the elements in the list
print(list(map(lambda c: c[::-1],words)))
