# Normal tuple
# the indexing values are easier to remember when the number of elements are lesser
# but when the tuple is large it will caus confusion while fetching elements from
# index values

t1 = (21,34,5,6,3,3,3,3,4,6)
print(t1)

print(t1[0])
print(t1[2])

# NamedTuples: along with the index values it will also assign the names for each element
# It creates new object types
from collections import namedtuple

# It is simlar to creating a class in this context 1st value in brackets is like class_name
# and attr_1 .. attr3 are like attributes
cat = namedtuple('cat','nails eyes color')

john = cat(nails='pointy',eyes="blue",color='grey')

# We can use the tuple values like we use in class
print(john.nails)

# We can also print multiple attributes
print(john.nails,john.eyes, john.color )
print(john)

# We can also use indexing like normal tuple
# it will return value present at that index
print("john[1]: ",john[1])
# OP: john[1]:  blue

# Example 2
emp = namedtuple('emp', 'id name email addr')
dave = emp(id =101, name='dave',email='dave@gamil.com',addr='india' )

# We can also print whole tuple value
print(dave)
