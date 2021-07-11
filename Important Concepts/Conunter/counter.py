"""
Counter
A Counter is a dict subclass for counting hashable objects.
It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values. 
Counter is a subclass of dict that’s specially designed for counting hashable objects in Python
It’s a dictionary that stores objects as keys and counts as values.
"""

word = 'mississippi'
word_counter = {}

for char in word:
    # Here we will check if the character is present in our empty dictionary
    if char not in word_counter:
        # If its not present then add the character to the dictionary and add the initial value to 0
        word_counter[char] = 0
    # If its presnt already then we can assume that we are revisiting the char so increment it by 1
    word_counter[char] += 1

print(word_counter)

# Solving it by using count objects (Using .get method from dict)
counter_next = {}
for char in word:
    counter_next[char] = counter_next.get(char, 0) + 1

print(counter_next)

# Solving it using defaultdict
from collections import defaultdict, Counter

counter_3 = defaultdict(int)

for letter in word:
    counter_3[letter] += 1
print(counter_3)

### Counter
"""
Input parameters: Iterable or hashable objects 
Counter internally iterates through the input sequence, counts the number of times a given object occurs, and stores objects as keys and the counts as values.
"""

# Counter iterates over "mississippi" and produces a dictionary with the letters as keys and their frequency as values.
counter_4 = Counter(word)
print(counter_4)

# We can also paas the list as an argument
counter_5 = Counter(list(word))
print(counter_5)

# Creating couter instances with starting values
letters = Counter({"i": 4, "s": 4, "p": 2, "m": 1})
