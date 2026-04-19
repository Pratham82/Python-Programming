# Negative indices
# Index from the end of the sequence using negative numbers. 
# The last element is at index -1

l1 =[2343,54,6456,546,466,898,56,78,21]
# for accessing the last index of the list we can provide -1 as an argument
print("List l1: ",l1)
print("Last index: ",l1[-1])

# Slicing 
# Extended form of indexing for referring to a portion of a list or other sequence
# Syntax: a_list[start:stop]

print("Elements from index 2:4 ",l1[2:4])
# O/P: Elements from index 2:4  [6456, 546]

print("Elements except first and last index: ",l1[1:-1])
# O/P: Elements except 1st and last index:  [54, 6456, 546, 466, 898, 56, 78]

print("Elements onwards second index till the last end: ",l1[2:])
# Elements onwards second index:  [6456, 546, 466, 898, 56, 78, 21]

print("Elements from  first index till the second index: ",l1[2:])
# Elements from  first index till the second index:  [6456, 546, 466, 898, 56, 78, 21]

print("Retrieve all the elements from the list: ",l1[:])
# Retrieve all the elements from the list:  [2343, 54, 6456, 546, 466, 898, 56, 78, 21]

# Copying a list 
# Assign operator does not copies an object it copies a reference of an object

# The is operator compares the identity
# the == operator compares the values of two objects.
l2 = l1
l3 =l1[:]

print ("l1: ",l1)
print("l2: ",l2)
print("l3: ",l3)

print("l1==l2: ",l1==l2)
print("l1 is l2: ",l1 is l2)

print("l1==l3: ",l1==l3)
print("l1 is l3: ",l1 is l3)

# Another ways of copying
l4 = l1.copy()
print("l4: ",l4)

l5 = list(l1)
print("l5: ",l5)

"""
All these techniques performs shallow copy i.e they create a new list containing the same object referenc to the source list, but they don't copy the referred to objects
"""
a= [[24,55],[45,665,342]]
b= a[:]
print("a is b: ", a is b)
print("a == b: ", a == b)

print ("a[0]: ",a[0])
print ("b[0]: ",b[0])
print ("a[1]: ",a[1])
print ("b[1]: ",b[1])

# Changing list a will affect b
a[0].append(99)
print("a: ",a)
print("b: ",b)

# But assgining a new value to the list will not change the other list
a[0] =[44,55]
print("a[0]: ",a[0])
print("b[0]: ",b[0])

print("list a: ",a)
print("list b: ",b)

# Lists supports repetition using multiplicationoperators
# Used for initialzing a list of a size known in advance with constant value

l1 = [23,45,556]
l2 = l1 * 3
print("l2: ",l2)

l4 = [2] *10
print(l4)

# Creating nested list

# When we modify the next list which has the same element it affects all elements because each element of the outlist is a reference to the same nested list
l5 =[[1,2]] * 5
print("l5: ",l5)
l5[1].append(9999)
print("after modifying l5: ",l5)

# The same does not happen with this list because all the elements are not same and refers to different objects
l5 =[[454,787],[121,454],[64,548],[456,789],[6484,878],[454,789]]
print("l5: ",l5)
l5[1].append(9999)
print("after modifying l5: ",l5)

# list.index()
# Find the location orf an object in a list
# Returns the index of the first list element  which is equal to the argument 

l6=[5454,54,454,554,878,51,65,487,454,54]
print("Index of 454: ",l6.index(454))

str1 ="Today's a beautiful day!, lets have some tea." 
# We can also do the split while creating sting 
# str1 ="Today's a beautiful day!, lets have some tea." .split()
str1_splitted =str1.split()
print(str1_splitted)
# Here the str_splitted will be stored in a list
print("Index of beautiful: ",str1_splitted.index("beautiful"))
print("Element present of index 3: ",str1_splitted[4])

# If the value is trying to retrieve is not present in the list we will get an error
# print("Index of beautiful: ",str1_splitted.index("handsome"))

# Count: counts the occurrence of the value provided 
print("Number of spaces in the list: ",str1.count(" "))

# in:  Checks if the element is present in the provided list 
print("Does the word 'beautiful' is present in str_spiltted?: ", "beautiful" in str1_splitted)

# not in:  Checks if the element is not present in the provided list 
print("Does the word 'beautiful' is not present in str_spiltted?: ", "beautiful"  not in str1_splitted)

# del: Removes an element from a list by index
# syntax: del a_list[index]

del str1_splitted[2]
print ("After deleting an element from a string ")
print(str1_splitted)

# Remove method
# syntax: list_a.remove("element")
print ("After removing an element from a string ")
str1_splitted.remove("lets")
print(str1_splitted)

# list.insert(): insert an item into a list. Accepts an item an the index of the new item
# syntax: list.insert(index,"new_string")
str2= "This is string 2, we can perform normal string operations on it.".split()
print(str2)
# here the new string will be added in the start of the string.
str2.insert(0,"This is newly added string")
print(str2)

# Reversing a list
list1 = [45,11,4,45,124,877,641]
print("List: ",list1)
list1.reverse()
print("Reversed list: ",list1)
"""
Sorting list
key parameter to list.sort()
1. Can be callabe object that accepts a single parameter
2.  Items passed to callable and sorted on its return value

"""

list1.sort()
print("List 1 after sorting(in ascending order): ",list1)

list1.sort(reverse=True)
print("List 1 after sorting(in descending order): ",list1)

str1= "This is new string which we are going to use for sort using key".split()
str1.sort(key=len)
print("List 1 after sorting(in ascending order): ",str1)
" ".join(str1)
print(str1)

# Reversing and sorting into copies
# reversed() and sorted() are out odf place equivalents to list.reverse() and list.sort()
# They retrun a reverse iterator and a new list, respectively
ls1 =[452,77,889,445,545,87,98]
ls2 = sorted(ls1)
print("ls1: ",ls1)
print("ls2: ",ls2)

ls1 =[452,77,889,445,545,87,98]
ls2 =reversed(ls1)\
#it will give us list_reverseiterator
print("ls1: ",ls1)
print("ls2: ",ls2)
# Passing the list_reverseiterator inside the constructor of list
print("ls2 using list(): ",list(ls2))
