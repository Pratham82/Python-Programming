# Strings are immutable
# The variables which are assigned to a strings are actually 
# object references and not the objects inself 

#Concatenation in strings
str1 = "New "+"York "+"city"
print(str1)

# Augmented assignment operator

str1= "New "
str1+= "York "
str1+= "City"

print(str1)


"""
# Use of join() method

1. Concatenation with + results in temporaries
2. str.join() inserts a seperator between collection of strings
3. Call join on seperator string
"""

# Joining the strings
colors =";".join(["Red","Yellow","Green","Blue"])
print(colors)

# Splitting the strings
print(colors.split(";"))

# Empty string seperators
str1= "".join(["Programming ","Language"])
print(str1)

# Partitioning: It splits the word in three parts, seperator, part before and after the seperator
# It returns tuple
str2= "Unbelievable"
print(str2.partition('bel'))

# String formating

str3 = "I have {} computers for work and {} of them is apple macbook."
print(str3.format("three","one"))

# keyword arguments in formating 
str4 = "Today' temperature is {deg} and {fh}"
print(str4.format(deg="30 degree celsius",fh="86 fahrenheit"))

val =22
str5= "My age is {} years."
print(str5.format(val))

# Literal string interpolation (-strings), from python 3.6 and later
# They are use to embed expressions inside literal strings, using a minimal syntax

# python expression can be added into the curly braces and they are evaluated and inserted at runtime
str6 = f"He drives {3*1} times a day"
print(str6)

import datetime
time1=f"The current time is {datetime.datetime.now().isoformat()}."
print(time1)

import math
math1= f"Math constants pi: {math.pi},e: {math.e}."
print(math1)