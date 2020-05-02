str_old = input("Enter string to reverse: ")

# Using for loop

def Rev(str_old):
    str_new = ""
    for i in str_old:
        str_new = i + str_new
    return str_new


print("Original string: ", str_old)
print("Reversed string: ", Rev(str_old))

# Using while loop
s1 = input("\nEnter string to reverse: ")
def Rev2(s):
    s_em=''
    i=len(s1)-1
    while i >=0:
        s_em = s_em + s1[i]
        i =i-1
    return s_em

print("Original string: ", s1)
print("Reversed string: ", Rev2(s1))

# Using extended slicing
s_in = input("\nEnter string to reverse: ")
def Rev3(s):
    return s[::-1]

print("Original string: ", s_in)
print("Reversed string: ", Rev3(s_in))
