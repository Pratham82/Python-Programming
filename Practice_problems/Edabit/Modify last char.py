# Modifying the Last Character
# Create a function which makes the last character of a string repeat n number of times.
# modify_last("Hello", 3) ➞ "Hellooo"
# modify_last("hey", 6) ➞ "heyyyyyy"


def modify_last(txt, n):
	return txt[:-1]+txt[-1]*n

print(modify_last("Hello", 3))