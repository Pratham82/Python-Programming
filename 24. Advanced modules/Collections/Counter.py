# Collections module: is a a built in module that implements specialized container 
# datatypes providing alternatives to python's general purpose built-in containers.

# Counter: is a dictionary subclass which helps counting hashable objects.

from collections import Counter

l1 =[1,2,3,4,523,2,1,3,41,3,5,5]

# Counter holds the unique values with number of occurrence
c = Counter(l1)
print(c)
