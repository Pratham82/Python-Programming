# Half, Quarter and Eighth
# Create a function that takes a number and return a list of three numbers: half of the number, quarter of the number and an eighth of the number.

def half_quarter_eighth(n):
	return [n / 2, n / 4, n / 8]


print(half_quarter_eighth(6))

# Take range and add it to an array

def CreateArray(n):
	l1 =[]
	for i in range(1,n+1):
		l1.append(i)
	
	return l1

print(CreateArray(10))