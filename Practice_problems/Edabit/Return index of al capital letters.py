# Return the Index of All Capital Letters
# Create a function that takes a single string as argument and returns an ordered list containing the indices of all capital letters in the string.

# Examples
# index_of_caps("eDaBiT") ➞ [1, 3, 5]

# index_of_caps("eQuINoX") ➞ [1, 3, 4, 6]

def index_of_caps(word):
	l1 = []
	splitted = list(word)
	for i in splitted:
		if i.isupper() == i:
			l1.push(i)
	
	return l1

print(index_of_caps("eDaBiT"))
