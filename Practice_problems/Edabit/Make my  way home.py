# Make My Way Home
# You will be given a list, showing how far James travels away from his home for each day. He may choose to travel towards or away from his house, so negative values are to be expected.

# Create a function which calculates how far James must walk to get back home.
from functools import reduce

def distance_home(lst):
	return abs(reduce(lambda x, y: x + y, lst))

print(distance_home([-1, -4, -3, -2]))
print(distance_home([3, 4, -5, -2]))