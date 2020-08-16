# Slightly Superior
# You will be given two extremely similar lists, but exactly one of the items in a list will be valued slightly higher than its counterpart (which means that evaluating the value > the other value will return True).

# Create a function that returns whether the first list is slightly superior to the second list.

def is_first_superior(lst1, lst2):
	check = True
	for i in range(len(lst1)):
		# print('lst1: ' , lst1[i], "lst2:", lst2[i])
		if lst1[i] < lst2[i]:
			check = False
			break
	if lst1 == lst2:
		check =  False
	return check


print(is_first_superior(["a", "d", "c"], ["a", "b", "c"]))
print(is_first_superior(["zebra", "ostrich", "whale"], ["ant", "ostrich", "whale"]))

print(is_first_superior([1, 2, 3, 4], [1, 2, 4, 4]))
print(is_first_superior([True, 10, 'zebra'], [True, 10, 'zebra']))