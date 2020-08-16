# Nth Star Number
# Create a function that takes a positive integer and returns the nth "star number".

# A star number is a centered figurate number a centered hexagram (six-pointed star), such as the one that Chinese checkers is played on.

def star_number(n):
	return 6*n*(n-1)+1