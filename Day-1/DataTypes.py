# Assigning values
# We don't have to explicitly define data types it happens automatically
print('Numbers\n--------------')
num1 = 234
num2 = 2434.46
name1 = 'John Snow'

print(num1)
print(num2)
print(name1)

# Multiple Assignment

a= b=c=d=1
print(c)

a,b,c,d = 12,44,546, "Var 4"
print(d)

'''
Data types in python:
   1. Numbers
   2. Strings
   3. List 
   4. Tuple
   5. Dictionary
'''
# 1. Numbers
number1 = 3423
number2 = 234

print(number1)
print(number2)
# del statement can be used to delete single or multiple objects

# 2. Strings
'''
Operators
1. Slice operator: [] & [:]
2. Concatenate: (+)
3. Repetition (*)
'''
print('Strings\n--------------')
str1 = "This is the Testing string"
print(str1)         # Prints complete string
print(str1[0])      # Prints first character of the string
print(str1[3:6])    # Prints characters starting from 4th to 6th
print(str1[2:])    # Prints string starting from 3rd character
print(str1 * 2)      # Prints string two times
print(str1 + " New concatenated String ") # Prints concatenated string

# List
'''
Operators
1. Slice operator: [] & [:]
2. Concatenate: (+)
3. Repetition (*)
Start of list [0]
End of the list[-1]
'''
list = ['noraml 1', 7834, " snow", 45641.54, 'john', 70.2 ]
tinylist = [123, 'john']

print('Lists\n--------------')
print(list)             # Prints complete list
print(list[0])          # Prints first element of the list
print(list[1:3])        # Prints elements starting from 2nd till 3rd
print(list[2:])         # Prints elements starting from 3rd element
print(tinylist * 2)     # Prints list two times
print(list + tinylist)  # Prints concatenated lists


# Tuple
'''
It is similar to the list. but for its declaration we use parenthesis()
Tuples cannot be updated like lists
'''
print()
print('Tuples\n--------------')
tuple1 = (342,35.54564,"new1",211,"FIle34",'Rock',2352)
tinyTuple1 = (2353,"yash")
print(tuple1)             # Prints complete list
print(tuple1[4])          # Prints fifth element of the list
print(tuple1[1:3])        # Prints elements starting from 2nd till 3rd
print(tuple1[2:])         # Prints elements starting from 3rd element
print(tinyTuple1 * 2)     # Prints list two times
print(tuple1 + tinyTuple1) # Prints concatenated lists


#Dictionary
print()
print("Dictionary\n--------------")
'''
Similar to hashtable. 
Dictionaries are enclosed by curly braces ({ }) 
and values can be assigned and accessed using square braces ([])
'''

dict1 ={'student 1':123,'Lecture 34':411,'Food':'Category'}
print(dict1)              #Printing whole dictionary
print(dict1['student 1']) # Prints value for 'Student 1' key
print(dict1.keys())       # Prints all the keys in dictionary
print(dict1.values())     # Prints all the values in dictionary

