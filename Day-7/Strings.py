# Strings in python are used to store textual information 
# Strigs can be written in single quotation marks or double quotation marks 
# We can display string literals using print() function
# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.


s1 = "This is example string 1"
s2 = 'This is example string 2'

print(type(s1))
print(type(s2))

print (s1)
print (s2)


s3 = """
    This is multiline string.
    We can write multiple line in this string.
    We can implement it by tripple quote in the code
    """
print(s3)

'''
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.

'''

# Mehtods in string

# Capitalize method: This method returns a copy of a string with only its first character capitalized
s3 = '  this is string s3  '
print("Original string: ", s3)
print("Capitalized string: ",s3.capitalize())

# len() function, It is used to get the length of the string 

print("Lentght of string s3: ",len(s3))

# strip() method, Remves the whitespaces from the string

print("String s3 without white spaces: ", s3.strip())


# replace(), replaces 

print(s3.replace('h','m'))


# check method, checks if the certain chracter or phrase is available in string 
s4 = "Once its done, you can perform the following operation."
print("String s4: ", s4)
i="done" in s4
print("Does string s4 containes 'done': ",i)

# We cannot combine strings directly, but we can use format method for combine different data types.
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are
age = 34
str1 = "Hi my name George, and my age is {} "
print(str1.format(age))

# We can use format method in a string to take unlimited amount of arguments

a = 5
b = "XPS 7780"
c = 1200

str2 = "I want {} units of Dell {} for {} doallrs."
print(str2.format(a,b,c))

# Wec can explicitly metion the parameters so the order is correct.
str3 = "I want to place order of {1} , {0} units which are priced at {2} doallars"

print(str3.format(a,b,c))

# Escape charcters: To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.
# An example of an illegal character is a double quote inside a string that is surrounded by double quotes

#ex1 = "We cannot add "this" in the statement"
# We can solve this issue using escape characters
ex1 = "We can now add \"this\" in the statement."
print(ex1)


