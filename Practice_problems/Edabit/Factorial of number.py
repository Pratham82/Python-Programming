# Factorial of a Number
# Create a function that receives a non-negative integer and returns the factorial of that number.

def fact(n):
	return 1 if n == 0 else fact(n - 1) * n
	
print(fact(5))