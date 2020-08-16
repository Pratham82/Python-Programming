
# using reduce for adding numbers
val = reduce((lambda x, y: x + y), [1, 2, 3, 4, 5,], 0)
print(val)


# using reduce for sum of even numbers

val2 = reduce((lambda x, y: x + y), filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))

print(val2)