# Write a function that computes the volume of a sphere given its radius.

def vol(n):
    vol = 4/3 * 3.14 *(n*n*n)
    return f"Volume of sphere is: {vol}"

print(vol(12))


# Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_check(num,low,high):
    if num in range(low,high+1):
        print (f"{num} is in the range between {low} and {high}")
    else:
        print (f"{num} is not in the range between {low} and {high}")
    return num in range(low,high+1)
    
print(ran_check(7,2,7))

# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
def up_low(s):
    countUpper=0
    countLower=0
    for i in s:
        if i.isupper():
            countUpper= 1+countUpper
        elif i.islower():
            countLower=1+countLower
        else:
            pass
    print("Number of upper case character: ", countUpper)
    print("Number of lower case character: ", countLower)

up_low(s)

# Instructor's mehtod
def up_low(s):
    d={"upper":0, "lower":0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["upper"])
    print("No. of Lower case Characters : ", d["lower"])

up_low(s)


# Write a Python function to multiply all the numbers in a list.

def multiply(nums):
    mul = 1
    for i in nums:
        mul *= i 
    return mul


print(multiply([1,2,3,-4]))


# Write a Python function that checks whether a passed in string is palindrome or not.

def pallindrome(s):
    rev=''
    for i in s:
        rev = i +rev
    return s == rev 
    
print(pallindrome("aba"))
print(pallindrome('helleh'))


# Write a Python function to check whether a string is pangram or not.
import string
def ispangram(str1, alphabet=string.ascii_lowercase):
    for i in alphabet:
        if i not in alphabet:
            return False
    else: return True

print("-------------")
print(ispangram("The quick brown fox jumps over the lazy dog"))


# Instructor's method
import string

def ispangram(str1, alphabet=string.ascii_lowercase):  
    alphaset = set(alphabet)  
    return alphaset <= set(str1.lower())

print(ispangram("The quick brown fox jumps over the lazy dog"))
