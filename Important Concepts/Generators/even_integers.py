# function solution
def even_integers_function(n):
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(i)
    return result


# print(even_integers_function(10))


def even_interger_fn(n):
    return [i for i in range(n) if i % 2 == 0]


even_fn = lambda n: [i for i in range(n) if i % 2 == 0]


# Generator solution for finding the even numbers till the given range
def even_interger_generator(n):
    for i in range(n):
        if i % 2 == 0:
            yield i


# Writing the above function in generator expression
# This will return a generator object unlike in list comprehension which will return a list
even_integers_exp = (i for i in range(1, 11) if i % 2 == 0)

print(even_interger_fn(10))
print(list(even_interger_generator(10)))
print(even_fn(10))
print(even_integers_exp)
# print(even_fn_gen(10))

# Next paramete in generator object
event_integers = even_interger_generator(10)
print('--Printing next values')
# print(event_integers)
# print(event_integers.next)
