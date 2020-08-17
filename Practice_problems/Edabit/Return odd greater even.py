# Return Odd > Even
# Given a list, return True if there are more odd numbers than even numbers, otherwise return False.

def oddeven(lst):
	return len(list(filter(lambda x: x % 2 == 0, lst))) < len(list(filter(lambda x: x % 2 != 0, lst)))

print(oddeven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(oddeven([13452394823795273847528572346]) )