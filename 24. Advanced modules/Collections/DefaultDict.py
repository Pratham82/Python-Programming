# Defaultdict: its a dictionary like object which has all the methods of the 
# dictionary but takes first argument(default_factory) as the default data type
# It is faster than using dic_object.set_default method.

# A default dictionary will never raise KeyError. If the given key is not present 
# in the dictionary then it will return the value by default factory.

from collections import defaultdict

# Normal dictionary
d1 = {'v1': 1}
print(d1['v1'])

# If we try to print the key which is not present in the dictionary
# then we will get an error
# print(d1['v1ds'])


d2 = defaultdict(object)

# If we try to print the key one it will return following object:
# <object object at 0x00000204BB1C4BA0>
print(d2['one'])

# It will return default ky which is one
for i in d2:
    print(i)


# defaultdict with lambda functions

# This assignment suggests that if the value for a key is not provided then the
# default value for that key will be 0
d3 = defaultdict(lambda: 0)

d3['key1']
d3['key2']
# Output:
# defaultdict(<function <lambda> at 0x00000287A842C160>, {'key1': 0, 'key2': 0,})
print(d3)

d3['key1'] = 101
print(d3)
# After assigning the value it will be updated
# defaultdict(<function <lambda> at 0x000002E49F0DC160>, {'key1': 101, 'key2': 0})

for i in d3:
    print(i)

# This method will print out key, value pair
for i in d3.items():
    print(i)