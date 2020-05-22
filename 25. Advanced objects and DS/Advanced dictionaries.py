
#* Advanced Dictionaries

#* dictionary comprehension

dict1 = {'k1':1,'k2':2}

dict2 ={x:x**2 for x in range(1,11)}
print(dict2)

# assigning keys which are not based on the values
dict3 ={k:v**2 for k,v in zip(['a','b'],range(2))}
print(dict3)

#* Iteration over keys,values
for i in dict1.items():
    print(i)

#* Iteration over keys
for i in dict1.keys():
    print(i)

#* Iteration over values
for i in dict1.values():
    print(i)

