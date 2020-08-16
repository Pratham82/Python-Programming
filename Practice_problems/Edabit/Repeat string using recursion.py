# Recursion to Repeat a String n Number of Times
# Create a recursive function that takes two parameters and repeats the string n number of times. The first parameter txt is the string to be repeated and the second parameter is the number of times the string is to be repeated.


def repetition(txt, n):
	# return '' if n < 0txt elif n == 1 else repetition(txt[:-1], n - 1)
	if n < 0:
		return ''
	elif n == 1:
		return txt
	else:
		return txt+ repetition(txt, n - 1)
	# return 'test'



print(repetition("ab", 3))
