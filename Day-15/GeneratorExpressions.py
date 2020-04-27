''' Syntax:
 (expr(item) for item in iterable)
 Generators are single use objects
 Each time we call generator function we create a new generator object 
 To recreate a generator from a generator expression, you must execute the expresion.
'''
million_squares =(x*x for x in range(1,1000001))
print(million_squares)

# Directly creating generator expression
print(sum(x*x for x in range(1,10000001)))