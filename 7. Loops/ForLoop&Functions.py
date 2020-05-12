
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

# Iterating through a string of characters
for c in "Python":
    print "charchater in string: ", c

# Iterating through list
Colors =["Red", "Green", "Yellow","Blue","Violet"]

print("\nMethod 1:")
for col in Colors:
    print "Colors in list: ",col

# An alternative way of iterating through each item is by index offset into the sequence itself
print("\nMethod 2:")
for index in range(len(Colors)):
    print"Colors in list: ",Colors[index]
range

print "\nBreak statement"

# With the break statement we can stop the loop before it has looped through all the items:

# Checking the condition first and then printing the number
# This will not include thr number of break point
for col in Colors:
    if col== "Yellow":
        break 
    print col

# Checking the condition aftter and then printing the number
# This will  include the number of break point
print 
for col in Colors:
    print col
    if col== "Yellow":
        break 
    


print "\nContinue statement"

# With the continue statement we can stop the current iteration of the loop, and continue with the next:

for col in Colors:
    if col =="Yellow":   # Yellow will be skipped
        continue
    print col

# To loop through a set of code a specified number of times, we can use the range() function,
# range function returns sequence of elements from  0 by default and increments 1 by default
# range(n) is not the values of 0 to n, but the values 0 to n-1
# range(6) is not the values of 0 to 6, but the values 0 to 5.
print "\nrange() function"

for i in range(5):
    print i

# We can also add the staring value with range function range(2,6) in  which the loop starts from 2 but does not include 6

print
for i in range (3,6):
    print i 


# We can provide the increment value with the range function
print
for i in range (2,10,2):
    print i


# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
print
for i in range(6):
    print i
else:
    print"Finally finished!"

# For loop with conditional statements for finding prime number between 1-20
print"\n Prime numbers between 1 to 20"
for n in range(1,21):               # Iterating through  1 to 20
    for i in range(2,n):            # Iterating through  2 to n
        if n%i==0:                  # Finding first factor    
            j = n/i                 # Finding second factor   
            print n,"= ",i," * ",j
            break                   # To move to the next number, the #first FOR
    else:
        print n,"is a prime number" 
        