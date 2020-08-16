# Check if One Array can be Nested in Another
# Create a function that returns True if the first list can be nested inside the second.

def can_nest(list1, list2):
	sortedlist1 = sorted(list1)
	sortedlist2 = sorted(list2)
	return  sortedlist2[0] < sortedlist1[0] and sortedlist1[-1] < sortedlist2[1]

print(can_nest([3, 1], [4, 0]))  #True

print(can_nest([9, 9, 8], [8, 9]))
print(can_nest([1, 2, 3, 4], [0, 6]))