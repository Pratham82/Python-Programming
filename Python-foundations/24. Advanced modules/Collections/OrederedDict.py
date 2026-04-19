from collections import OrderedDict
# OrderedDict: unlike normal dictionary, this dictionary will retain the insertion order.

# Normal dictionary
d1 = {}
d1['peter']= 101
d1['john']= 102
d1['jess']= 103
d1['jeffery']= 104
d1['joe']= 105
d1['larry']= 106
d1['shanks']= 107
d1['mark']= 108
d1['steve']= 109
d1['Bill']= 110
d1['shanks']= 111
d1['shanks']= 111

# The value will no be in insertion order
for i in d1.items():
    print(i)

d1_ord = OrderedDict()

d1_ord['peter']= 101
d1_ord['john']= 102
d1_ord['jess']= 103
d1_ord['jeffery']= 104
d1_ord['joe']= 105
d1_ord['larry']= 106
d1_ord['shanks']= 107
d1_ord['mark']= 108
d1_ord['steve']= 109
d1_ord['Bill']= 110
d1_ord['garry']= 111
  
print("Ordered dictionary: ")
for i in d1_ord.items():
    print(i)


# NOrmal dictionaries comparison
# As we can see the key values in both the dictionaries are same.
# So when we compare both the dictionaries it will retrun true 
# Because normal dictionaries only compares the values and not the order of insertion. 

dict1 = {}
dict1['a'] = 1
dict1['b'] = 2
dict1['c'] = 3

dict2 = {}
dict2['c'] = 3
dict2['a'] = 1
dict2['b'] = 2

print("dict1==dict2: ",dict1==dict2)


# When comparing the ordered dictionary will also check the insertion order 
# as well as the key values that's why in this case it will return false
print("Comaprison for ordered dictionary")
dict1 = OrderedDict()
dict1['a'] = 1
dict1['b'] = 2
dict1['c'] = 3

dict2 = OrderedDict()
dict2['c'] = 3
dict2['a'] = 1
dict2['b'] = 2
print("dict1==dict2: ",dict1==dict2)