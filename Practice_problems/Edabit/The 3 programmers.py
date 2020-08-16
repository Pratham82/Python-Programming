# The 3 Programmers Problem
# You hired three programmers and you (hopefully) pay them. Create a function that takes three numbers (the hourly wages of each programmer) and returns the difference between the highest-paid programmer and the lowest-paid.

def programmers(one, two, three):
	arr = [one, two, three]
	return max(arr) - min(arr)


print(programmers(33, 72, 74))