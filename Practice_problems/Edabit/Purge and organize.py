# Purge and Organize
# Given a list of numbers, write a function that returns a list that...

# Has all duplicate elements removed.
# Is sorted from least to greatest value.

def unique_sort(lst):
	unique = []
	[unique.append(i) for i in sorted(lst) if i not in unique]
	return unique
	# return list(dict.fromkeys(sorted(lst)))

print(unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]))  # [1, 2, 3, 4]
print(unique_sort([3, 6, 5, 4, 3, 27, 1, 100, 1]))