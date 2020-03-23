
#Python programming language assumes any non-zero and non-null values as TRUE, and if it is either zero or null, then it is assumed as FALSE value.

#if statements

n1 = 1323
if n1:
    print("Print if n1 is non zero")
    print("Test Line 1")

n2 = 0
if n2:                               
    #If the n2 is false then nothing will be printed from the same block
    print("Print if n2 is non zero")
    print("Test Line 2") 

#This will be printed because this line is different block
print("Final line")


n1 = 122
n2 = 223
if(n1 !=n2):
    print ("n1 is not equal to n2")


#if elif statements

if n1>n2:
    print "n1 is greater than n2" #Python 2 style  printing
elif n1<n2:    
    print "n1 is lesser than n2"


#if elif else statements

if n1>n2:
    print "n1 is greater thaan n2" #Python 2 style  printing
elif n1==n2:    
    print "n1 is equal to n2"
else:    
    print "n1 is lesser than n2"


#Nested if else

if n1>50:
    print"n1 is greater than 50"
    if n1>70:
        print"n1 is greater than 70"
    if n1>90:
        print"n1 is greater than 90"
    else:
        print"n1 is not greater than 50"


# pass 
a = 33
b = 200

if b > a:
    pass

# having an empty if statement like this, 
# would raise an error without the pass statement

# if with boolean

if n1>n2 and n2>n1:
    print "True"
else:
    print"false"

if n1>n2 or n2>n1:
    print "True"
else:
    print"false"
