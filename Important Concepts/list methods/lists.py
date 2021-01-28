list1: list = ["apple", "banana", "orange", "grapefruit", "grape", "pinapple"]

# 1. append: adds/appends the object at the end of the list
list1.append("watermelon")

print(list1)
# ['apple', 'banana', 'orange', 'grapefruit', 'grape', 'pinapple', 'watermelon']


# 2.  count: it takes the object as argument and returns the number of times object appeared in list
print(list1.count("apple"))
# 1

# 3. extend: it takes iterables as argument and modifies the original list
list1.extend(["pear", "dragonfruit"])
print(list1)
# ['apple', 'banana', 'orange', 'grapefruit', 'grape', 'pinapple', 'watermelon', 'pear', 'dragonfruit']

# 4. index: returns the index of the specified element in the list.
print("The index of orange in list is", list1.index("orange"))
# The index of orange in list is 2

# 5. reverse: reverses the list and updates the existing list
list1.reverse()
list1.reverse()
print(list1)

# 6. remove: removes the first mathing element from list
list1.remove("apple")
print(list1)
# ['banana', 'orange', 'grapefruit', 'grape', 'pinapple', 'watermelon', 'pear', 'dragonfruit']

# 7. pop: removes the item at the given index  by default removes from the list and returns the removed item.
list1.pop(-2)
print(list1)
# ['banana', 'orange', 'grapefruit', 'grape', 'pinapple', 'watermelon', 'dragonfruit']

# 8. insert: takes two arguments one is index and second is the object to enter in list
list1.insert(0, "newfruit")
print(list1)
# ['newfruit', 'banana', 'orange', 'grapefruit', 'grape', 'pinapple', 'watermelon', 'dragonfruit']
