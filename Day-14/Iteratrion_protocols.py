'''
Iteration protocols:
iterable: cam ne passed to iter() produce an iterator
iterator: can be passed to next() to get the next value in the sequence
'''

iterable = ['Spring','Summer', 'Autumn','Winter']
iterator = iter(iterable)
# next is built in method in iterator
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


# Stopping iteration with an exception
# A single end:  sequences only have on ending, after all, so reaching it is exceptional.
# Infinite sequences: Finding the end of infinite sequence would be truly exceptional.

def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterator is empty")

print(first(['1st','2nd','3rd']))
print(first({'1st','2nd','3rd'}))
# This line will cause an error 
# print(first(set()))