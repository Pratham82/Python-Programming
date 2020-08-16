# Sort Numbers in Ascending Order
# Create a function that takes a list of numbers and returns a new list, sorted in ascending order (smallest to biggest).

# Sort numbers list in ascending order.
# If the function's argument is None or an empty list; return an empty list.
# Return a new array of sorted numbers.


def sort_nums_ascending(lst):
	return sorted(lst) if len(lst) > 0 else []
	#  
	
print(sort_nums_ascending([1, 2, 10, 50, 5]))