word = "Python 3.5"

for i in word:
    print (i)

# We can not directly iterate on a string
# For iterating over a string we have to convert a string into a generator
print("____________")
word_iter = iter(word)
print(next(word_iter))
print(next(word_iter))
print(next(word_iter))
print(next(word_iter))