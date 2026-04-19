"""
Set:   are unordered collection of unique elements.
Sets are mutable.
Elements inset must be immutable.
"""
# Creating a set
set1 ={213,454,554,6,78,781,2,31,34}
print("set1 :",set1)

print("Type of set1:",type(set1))

# For creating an empty set we have to use set constructor
set2 = set()
print("Set2:",set2)

# We can add any iterable series in set
set3 =set([65546,657,809,980,34,346,478,89,43,44,75])
print("Set3:",set3)

# Set is mainly used to remove duplicate elements in the series of objects
l1 = [44,54,1,5,45,41,564,54167,89,4,54,1,5,44]
print("List l1:",l1)
# Form the output we can see the duplicate elements are removed.
set4= set(l1)
print("Set4:",set4)
# O/p  Set4: {1, 4, 5, 41, 44, 45, 564, 54, 54167, 89}

# Iterating over set
for i in set4:
    print(i)

# Adding elements in set
set4.add(999)
print("After adding element: ")
print("set4:",set4)

# Updating 
set4.update([111,444])
print("set4 after updating:",set4)

# Delete method
set4.remove(999)
print("set4 after deleting:",set4)

# Set algebra
blue_eyes={"John","Rob","Brian","Lee","Sean"}
blond_hair={"Harry","Drake","Rob","Jake","John"}

# Uninon 
print("Union:",blue_eyes.union(blond_hair))
print("Equality:",blue_eyes.union(blond_hair)==blond_hair.union(blue_eyes))

# Intersection
print("Intersection:",blond_hair.intersection(blue_eyes))
print("Equality: ",blond_hair.intersection(blue_eyes)==blue_eyes.intersection(blond_hair))

# Difference
print("Difference:",blond_hair.difference(blue_eyes))
print("Equality: ",blond_hair.difference(blue_eyes)==blue_eyes.difference(blond_hair))

# Symmetric difference
print("Symmetric difference:",blond_hair.symmetric_difference(blue_eyes))
print("Equality: ",blond_hair.symmetric_difference(blue_eyes)==blue_eyes.symmetric_difference(blond_hair))

# Subset
print(blue_eyes.issubset(blond_hair))
print(blond_hair.issubset(blue_eyes))

# Is superset
print(blue_eyes.issuperset(blond_hair))

# Disjoint
print(blue_eyes.isdisjoint(blond_hair))