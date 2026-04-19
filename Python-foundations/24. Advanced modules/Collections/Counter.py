# Collections module: is a a built in module that implements specialized container 
# datatypes providing alternatives to python's general purpose built-in containers.

# Counter: is a dictionary subclass which helps counting hashable objects.

from collections import Counter

l1 =[1,2,3,4,523,2,1,3,41,3,5,5]

# Counter creates dictionary of the the unique values with number of occurrence
c = Counter(l1)
print(c)

s1 = 'assasisnscreedvalhala'
c  = Counter(s1)
print(c)

# Counting word in a sentence
sentence_1 = 'This is one of the example of example that is'
s2 = sentence_1.split()
c2 = Counter(s2)
print(c2)

# returns most common words 

# If arguments is not passed it will give all words
print(c2.most_common())

# We can also pass number of words so it will return the that many words
print(c2.most_common(3))

# Returns the total words in a sentence
print(sum(c2.values()))

print(c2.clear())
print(c2)

"""
Common methods which can be used with Counter() object

sum(c.values())                 # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
c.most_common()[:-n-1:-1]       # n least common elements
c += Counter()                  # remove zero and negative counts
"""

s3 = 'lorem ipsum lorem ipsum is an ancient text. lorem'

# Spliting sentence into words
s3 = s3.split()

# Creating counter
s3_counter = Counter(s3)
print("s3 as a counter: ",s3_counter)

# s3_counter.clear()
# If we clear the counter variable, only Counter() will be returned
# O/P: Counter()

# Conveting counter to a dictionary
s3_dict = dict(s3_counter)
print("s3 as a dictionary: ",s3_dict)
 
# Conveting counter to a set
s3_set = set(s3_counter)
print("s3 as a set: ",s3_set)

# Convert to a list of (elem, cnt) pairs
s3_items = s3_counter.items()
print("s3 items: ", s3_items)

# least count of elements
# here the first value in list is count of numbers, 
s3_most_comm =s3_counter.most_common()[:-3-1:-1]
print(s3_most_comm)

# removes non zero count
s3_counter += Counter()
print(s3_counter)

