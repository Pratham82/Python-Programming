set1 = set()
set1.add(45)
set1.add(77)
set1.add(56)
set1.add(34)
set1.add(47)
set1.add(34)
set1.add(34)
set1.add(34)

# Set does not contain duplicate elements
print("set1: ",set1)

#* Clearing a set
# set1.clear()
# print(set1)

#* Copy
set2 = set1.copy()     # Changes done on original set will not affect new set
print("set2: ",set2)  

set2.add(784)
print(set2)
#* Diff  finds out the different between two sets
# checks if inner set has the all values of outer set
print(set1.difference(set2)) 
print(set2.difference(set1)) 

#* diff update: This method removes the common elements from the list
set3 ={34,56,77}
set4 ={34,97,45}

# Removes the commmon element of the outer set, and add the common element into 
# inner set
set3.difference_update(set4)

print(set3)
print(set4)

# * discard: Removes the passed argument from the set

set5 ={67,57,68,979,89,8,89}
set5.discard(67)
print(set5)

# * intersection returns the common elements from both the sets
s_1 ={454,45,56,76,7,434,34}
s_2 ={116,76,7,435,678}

print(s_1.intersection(s_2))
print("s_1:",s_1)
print("s_2:",s_2)

# * intersection update keeps the common elements of the outer set and removes
# * everything else
s_1.intersection_update(s_2)

print("s_1:",s_1)
print("s_2:",s_2)
"""
o/p:
s_1: {76, 7}
s_2: {678, 7, 76, 435, 116}
"""

# * isdisjoint : This method will return True if two sets have a null intersection.

s_1 ={454,45,56,76,7,434,34}
s_2 ={116,76,7,435,678}
s_3 ={14,75,5,4,88}

print(s_1.isdisjoint(s_2))
print(s_1.isdisjoint(s_3))

#* issubset This method reports whether another set contains this set.

s_1 ={112,113,114,115,116,117,118}
s_2 ={115,113,114,112}
 
print(s_1.issubset(s_2))
print(s_2.issubset(s_1))

# * issuperset This method will report whether this set contains another set.

print(s_1.issuperset(s_2))
print(s_2.issuperset(s_1))

#* symmetric_difference and symmetric_update
# Return the symmetric difference of two sets as a new set.(i.e. all elements that are in exactly one of the sets.)
print("s_1:",s_1)
print("s_2:",s_2)
print(s_1.symmetric_difference(s_2))
print(s_2.symmetric_difference(s_1))

print(s_1.symmetric_difference_update(s_2))


#* Union: return union of two sets
print(s_1.union(s_2))


#* Update: Update a set with the union of itself and others.
s_2.update(s_1)
print(s_2)
