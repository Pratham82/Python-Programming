from array import *

a1 =array('i',[])

n = int(input("Enter length of the arrray: "))

# Getting length and values of array from user

for i in range(n):
    num =int(input("Enter value: "))
    a1.append(num)

print(a1)

f2 = int(input("Enter number to find in our array and get its index: "))

ind =0
for i in a1:
    if i == f2:
        print(f"Value found at index {ind}")
        break
    ind+=1


if i!=f2:
    print("Value not found")


print("Finding index of value using in built function",a1.index(f2))