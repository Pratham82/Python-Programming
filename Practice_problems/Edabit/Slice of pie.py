# Slice of Pie
# Create a function that determines whether or not it's possible to split a pie fairly given these three parameters:

# Total number of slices.
# Number of recipients.
# How many slices each person gets.

def equal_slices(total, people, each):
	return people * each <= total


print(equal_slices(11, 5, 3)) # False
print(equal_slices(11, 5, 2)) # True