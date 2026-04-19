
# * Strings

# capitalize: capitalize the 0th character
s1 =  'testing string'
print(s1.capitalize())


# * Location and counting

# count: counts the occurrence
a = s1.count('e')
print(a)

# find: finds the first occurrence
b = s1.find("t")
print(b)

# * Formatting

# Center : center the given string and passed in number of characters
# The fill character must be exactly one character long
s3 ="Python programming"
c = s3.center(35,'*')
print(c)

# expandtabs
s4 ="Hi\tthere"
print(s4)
s4 ="Hi\tthere".expandtabs()
print(s4)

# is check methods

# isalpha: 
s5 = 'String'
s6 = 'String normal' # space is also considered as special char
print(s5.isalpha())
print(s6.isalpha())

# isalnum

print(s5.isalnum())
print(s6.isalnum())

# islower: checks if all characters in the string are lower case
low ="string"
print(s6.islower())
print(low.islower())

# isupper: checks if all characters in the string are lower case
up = "STRING"
print(s6.isupper())
print(up.isupper())

# isspace: check if the string has a whitespace
sp ="This string"
print(sp.isspace())

# istitle: Checks if the given string is title case string
title1 = 'This'
print(title1.istitle())

#endwith: checks if the string ends with the given character  
st1 ="pirated"
print(st1.endswith("d"))


# * Built-in regex

# split: splits the string on every occurrence of character
st2 = 'helloworld'
print(st2.split('o'))  

# partition : gives the head(charaters before separator) sep(seperator) and 
# tail(characters after seperator)
# only splits string after 1st occurrence
print(st2.partition("o"))

