"""
Dictionaries: A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
1. Keys must be unique in the dictionaries
2. Values can be same.
3. Internally dictionaries maintains te pairs of references to keys and values
4. Keys must be immutable
5. Values can be mutable
6. Order of elements in the dictionaries is random
"""
# We can use  ict constructor to convert another types to dictionaries.
Data_1 =[("John",24),("Rob",29),("Sansa",23),("Jamie",35)]
d = dict(Data_1)
print("Dictionary d: ",d)
print("Type of d:",type(d))
d2 = dict( Test1= "101", Test2="102", Test3="103", Test4="104")
print("Dictionary d2: ",d2)

# Copying is similar to list. Copying the references to key and value references not the actual objects.

d3 = d2.copy()
print("d3: ",d3)

d4 = dict(d2)
print("d4: ",d4)

# Update method in dictionary.
# adds entires from one dictionary into another.
# Call this on the dictionary that is to be updated.

d3 = {"Google": 457,"Amazon":995,"Microsoft":787,"Facebook":445}
d4 = {"Uber":223,"Netflix":664,"Verizon":224}
print("Dictionary d3: ",d3)
print("Dictionary d4: ",d4)
d3.update(d4)
print("Updated dictionary d3: ",d3)

# Modifying values in dictionary
d3.update({"Google":999})
print("dictionary d3 after updating: ",d3)

# Dictionary iteration
# Dictionaries yield the next  key to each iteration

# Printing only keys
print("\nPrinting only keys method 1: ")
for key in d3:
    print(key)

print("\nPrinting only keys using .keys(): ")
for key in d3.keys():
    print(key)

print("\nPrinting only values method 1: ")
for value in d3:
    print(d3[value])

print("\nPrinting only values using .values(): ")
for value in d3.values():
    print(value)

print("\nPrinting key and values")
for key in d3:
    print(f"{key}: {d3[key]}")

# Passing key in square bracket which will  give us value
print(d3["Google"])


# dict.items()
# Iterates over keys in tandem
# Yields a (key,value) tuple on each iteration

# Using dict.items90 with tuple unpacking
for key,value in d3.items():
    print(f"Key: {key}, Value: {value}")

# Deleting value sin dictionaries
d5 ={"Oneplus":111,"Samsung":112,"Xiomi":113,"LG":114,"RealMe":115}
print("Dictionary d5: ",d5)

del d5["Xiomi"]
print("\nAfter deleting:  ")
print("Dictionary d5: ",d5)

# Keys in the dictionaries although the values are modified.

