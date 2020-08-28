# Add the Index
# Given a list of numbers, create a function which returns the list but with each element's index in the list added to itself. This means you add 0 to the number at index 0, add 1 to the number at index 1, etc...

# Examples
# add_indexes([0, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4]

def add_indexes(lst):
	arr =[]
	for i in range(len(lst)):
		arr.append(lst[i] + i)
	
	return arr

print(add_indexes([0, 0, 0, 0, 0]))