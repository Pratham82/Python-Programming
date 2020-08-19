# Nth Smallest Element
# Given an unsorted list, create a function that returns the nth smallest element (the smallest element is the first smallest, the second smallest element is the second smallest, etc).

# example
# nth_smallest([1, 3, 5, 7], 1) ➞ 1
# nth_smallest([1, 3, 5, 7], 3) ➞ 5
# nth_smallest([1, 3, 5, 7], 5) ➞ None

def nth_smallest(lst, n):
	return  sorted(lst)[n-1] if len(lst)>= n else None

print(nth_smallest([1, 3, 5, 7], 3))
print(nth_smallest([1, 3, 5, 7], 5))