# Basic output function
# By default python’s print() function ends with a newline. A programmer with C/C++ background may wonder how to print without newline.


print ("Output")

# You can end a print statement with any character/string using this parameter.

# Does not works with python 2.7 , works with 3.0
print ("Hi this is ", end=' ' )
print ("Python Tutorial",end=" ")

print()
print("www.tester", end="@")
print("gmail.com")


# sep:  
# seperator parameter: The separator between the arguments to print() function in Python is space by default (softspace feature) ,which can be modified and can be made to any character, integer or string as per our choice.

# Does not works with python 2.7 , works with 3.0

print('C','o','d','e','r', sep='')
print("C","o","d","e","r", sep=' ')
print('12','12','2012',sep="-")
print("prathamesh","gmail.com", sep= "@")