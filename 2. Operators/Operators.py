'''
Operators in python

Arithmetic Operators
Comparison (Relational) Operators
Assignment Operators
Logical Operators
Bitwise Operators
Membership Operators
Identity Operators
'''

# Arithmetic Operators
print("Arithmetic Operators")
a = 10
b = 20

print("Values: \na: 10\nb: 20")

c = a + b
print("a + b: ", c)

c = b - a 
print("b - a: ", c)

c = a * b
print("a * b: ", c)

c = b / a
print("a / b: ", c)

c = b % a
print("b % a: ", c)

#Exponent
c = a**3
print("a**2",c)

#Floor division (IT rounds up the value)
c = b//a
print("b // a",c)
print(' \n')

#Comparison operators
print("Comparison operators")
print("10 == 20: ",a==b)
print("10 != 20: ",a!=b)
print("10 > 20: ",a>b)
print("10 < 20: ",a<b)
print("10 >= 20",a>=b)
print("130 >= 130: ",130>=130)
print("130 <= 130: ",130<=130)

# Assignment Operators
num1 = 100
num2 = 200
print("Values: \nnum1: 100\nnum2: 200")
num1=num2
print("After operation \nnum1 = num2\nnum1 = ", num1)
print()
print("Values: \nnum3: 300\nnum4: 400")
num3 = 300
num4 = 400
#num3 = num3 + num4
num3+=num4
print("After operation\nnum3 += num4\n300 += 400\nnum3 = ",num3)

print()
print("Values: \nnum5: 500\nnum6: 600")
num5 = 500
num6 = 600
#num6 = num6 - num5
num6-= num5
print("After operation\nnum6 -= num5\n500 -= 600 \nnum6 = ",num6)
print()
print("Values: \nnum7: 10\nnum8: 8")
num7 = 10
num8 = 8
num7*= num8
print("After operation\nnum7 *= num8\n10 *= 8\nnum6 = ",num7)

print()
print("Values: \nnum9: 90\nnum10: 10")
num9 = 90
num10 = 10
num9/= num10
print("After operation\nnum9 / = num10\n 90 / = 10\nnum9 = ",num9)

print()
print("Values: \nnum11: 110\nnum12: 11")
num11 = 110
num12 = 11
num11 %= num12
print("After operation\nnum11 %= num12\n110 %= 11 \nnum11 = ",num11)

print()
print("Values: \nnum13: 4\nnum14: 3")
num13 = 4
num14 = 3
num13**= num14
print("After operation\nnum13 **= num14\n4 **= 3\nnum13 = ",num13)

print()
print("Values: \nnum15: 54\nnum16: 5")
num15 = 54
num16 = 5
num15//= num16
print("After operation\nnum15 //= num16\n54 //= 5\nnum15 = ",num15)

print()
print("Bitwise Operators")
a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
print('''
        Binary values
a = 60  0011 1100   
b = 13  0000 1101
''' )
c = 0

print("Binary AND ")
c = a & b;        # 12 = 0000 1100
print ("After operation\nc = a & b\nValue of c is: ", c,"\n")

print("Binary OR ")
c = a | b;        # 12 = 0000 1100
print ("After operation\nc = a | b\nValue of c is: ", c,"\n")

print("Binary XOR")
c = a ^ b;        # 12 = 0000 1100
print ("After operation\nc = a ^ b\nValue of c is: ", c,"\n")

print("Binary ones")
c = (~a)         # 12 = 0000 1100
print ("After operation\nc = (~a) \nValue of c is: ", c,"\n")

print("Binary Left shift")
c = a << b;        # 12 = 0000 1100
print ("After operation\nc = a << b\nValue of c is: ", c,"\n")

print("Binary Right shift")
c = a >> b;        # 12 = 0000 1100
print ("After operation\nc = a >> b\nValue of c is: ", c,"\n")


print("Logical operators\n ")

print('''num1 = 41
num2 = 32
''' )
print("41 and 32:",(num1 and num2))
print("41 or 32:",(num1 or num2))
print("not(41 and 32):",not(num1 and num2))


print("\nIdentity operators\n")
'''
is: Returns True if a sequence with the specified value is present in the object
is not: Returns True if both variables are not the same object
'''
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print('''x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
''')
print("x is z",x is z)

# returns True because z is the same object as x

print("x is y",x is y)

# returns False because x is not the same object as y, even if they have the same content

print("x == y",x == y)

# to demonstrate the difference between "is" and "==": this comparison returns True because x is equal to y

print("x is not z",x is not z)

# returns False because z is the same object as x

print("x is not y",x is not y)

# returns True because x is not the same object as y, even if they have the same content

print("x != y",x != y)

# to demonstrate the difference between "is not" and "!=": this comparison returns False because x is equal to y



print("\nMembership operators\n")
'''
in: Returns True if a sequence with the specified value is present in the object
not in: Returns True if a sequence with the specified value is not present in the object	
'''
list = ["Red","Yellow","Green","Blue"]
print("Red in list:","Red" in list)
print("Red not in list:","Red" not in list)


