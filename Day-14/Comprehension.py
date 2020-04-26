'''
Comprehension: Concise syntax for describing lists, sets and dictionaries.
Readable and expressive.
Close to natural language.
syntax: [expr(item) for item in iterable]
'''

words = 'This is test sentence 1, which we can break into words.'.split()

# Comprehension is enclosed in square brackets
print([len(word) for word in words])

# Equivalent syntax:
lengths =[]
for word in words:
    lengths.append(len(word))

print(lengths)

# The expression producing the new list's elements can be any Python expression.

from math import factorial
f= [len(str(factorial(x))) for x in range(20)]
print(f)

# Set comprehension
s= {len(str(factorial(x))) for x in range(20)}
print(s)

# Dictionary comprehension
# syntax:{ key_expr(item): value_expr(item) for item in iterable}
# Dictionary comprehensions don't work directly on dict sources.
# Using dict.items() to get keys and values from dict sources.

country_to_capital ={'United Kingdom':'London','India':'Delhi','United States':'Washington D.C'}

country_to_capital ={country: capital for country,capital in country_to_capital.items()}
print(country_to_capital)