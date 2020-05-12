# Normal way of adding string to an list

string1 = "Python is very easy"

arr1 = []

for i in string1:
    arr1.append(i)
    
print("arr1: ",arr1)

# Using list comprehension

arr2 =[i for i in string1]

print("arr2: ",arr2)

# Appending a string to a varibale

l1 = [ x for x in "Pythonicon"]
print("l1: ",l1)

# Appending ranges in a list

l2 = [n for n in range(11)]
print("l2: ",l2)

l3 = [n**2 for n in range(11)]
print("l3: ",l3)

# Even numbers in 0 to 100

l4 = [n for n in range (101) if n % 2 ==0]
print("l4: ",l4)

# Squre of only even numbers

l5 = [ n**2 for n in range(101) if n%2 ==0]
print("l5: ",l5)

# Converting celcius to fahrenheit

celcius = [5,12,21,34.5,40]
fahrenheit = [((9/5)* i +32)for i in celcius]
print("Fahrenheit: ",fahrenheit) 

# If else in list comprehensions

l6 = [x if x % 2 ==0 else 'ODD' for x in range(21)]
print("l6: ",l6)

# Nested loops in list comprehension

# Normal nested loop
list_1 =[]
for i in [2,4,6]:
    for j in [1,10,100]:
        list_1.append(i*j)

print("list_1: ", list_1)

# Nested loop in list comprehension

list_2=[x * y for x in [2,4,6] for y in [1,10,100]]
print("list_2: ",list_2)