
#* Advanced lists

#* append: appends an element to the end of a list
#* append: appends whole object at end
l1 =[223,455,6456,67]
l1.append(555)

print(l1)

#* count: count() takes in an element and returns the number of times it occurs in your list
print(l1.count(223))

#* extend: extends list by appending elements from the iterable(input as [])
l1.extend([343,456,2])
print(l1)

#* will return the index of whatever element is placed as an argument.
print(l1.index(455))

#*  insert: takes in two arguments: insert(index,object) This method places the object at the index supplied.
print(l1)
l1.insert(3,999)
print(l1)


#* pop which allows us to "pop" off the last element of a list. 
# However, by passing an index position you can remove and return a specific element.
l1.pop() # removed last element 
print(l1)
l1.pop(2) # removed element on 2nd index
print(l1)

#* remove:method removes the first occurrence of a value
l2 =[111,111,111,111,112,113,114]
print(l2)
l2.remove(111)
print(l2)

#* reverse reverse the given list,  it affects your list permanently.
l2.reverse()
print(l2)

#* sort method will sort your list in place
l2.sort()
print(l2)