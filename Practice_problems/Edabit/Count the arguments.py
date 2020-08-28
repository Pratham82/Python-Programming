# Count the Arguments
# Create a function that returns the number of arguments it was called with.

# Examples
# num_args() ➞ 0

# num_args("foo") ➞ 1


def num_args(*args):
	return len(args)

print(num_args())