# Shuffle the Name
# Create a function that takes a string (will be a person's first and last name) and returns a string with the first and last name swapped.

def name_shuffle(txt):
	l1 = (txt.split(" "))
	l1.reverse()
	return " ".join(l1)


print(name_shuffle("Donald Trump"))