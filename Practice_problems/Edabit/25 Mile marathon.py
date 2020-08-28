# 25-Mile Marathon
# Mary wants to run a 25-mile marathon. When she attempts to sign up for the marathon, she notices the sign-up sheet doesn't directly state the marathon's length. Instead, the marathon's length is listed in small, different portions. Help Mary find out how long the marathon actually is.

# Return True if the marathon is 25 miles long, otherwise, return False.

# Examples
# marathon_distance([1, 2, 3, 4]) ➞ False

# marathon_distance([1, 9, 5, 8, 2]) ➞ True

def marathon_distance(*args):
	return sum(list(map(lambda x: abs(x), d)))  == 25


print(marathon_distance([1, 2, 3, -4]))
print(marathon_distance([1, 9, 5, 8, 2]))