
# We use input for taking taking input from user and making out program interactive

# Types of input:
# 1. raw_input(prompt): 
# 2. input(prompt): 

# raw_input(): 
# raw_input(): This function takes exactly what is typed from the keyboard, convert it to string and then return it to the variable in which we want to store.

n1 = raw_input("Enter the value: ")
print ("Entered value: ",n1)

n1 = raw_input("Enter your name: ")
print ("Hi",n1,"Welcome to python.")

#input(): This function first takes the input from the user and then evaluates the expression, which means Python automatically identifies whether user entered a string or a number or list. 
# If the input provided is not correct then either syntax error or exception is raised by python. 
'''
n2 = input("Enter Number: ")

n3 = input("Enter Name: ")

print "Type of number: ", type(n2)
print "Type of Name: ", type(n3)
'''
# Program to check input 
# type in Python 

num = input ("Enter number :") 
print(num) 
name1 = raw_input("Enter name : ") 
print(name1) 

# Printing type of input value 
print ("type of number", type(num)) 
print ("type of name", type(name1)) 
