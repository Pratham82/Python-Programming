# List Operation
# Create a function that takes three parameters and returns a list with the first parameter x, the second parameter y, and every number in between the first and second parameter in ascending order. Then filter through the list and return the list with numbers that are only divisible by the third parameter n.

def list_operation(x, y, n):
	l1 =[]
	for i in range(x, y+1):
		l1.append(i)
	return list(filter(lambda x: x % n == 0, l1))

print(list_operation(1, 10, 3))
print(list_operation(7, 9, 2))
print(list_operation(10, 50, 10))