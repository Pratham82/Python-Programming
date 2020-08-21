# Xs and Os, Nobody Knows
# Create a function that takes a string, checks if it has the same number of "x"s and "o"s and returns either True or False.

# Return a boolean value (True or False).
# The string can contain any character.
# When no x and no o are in the string, return True.

def XO(txt):
	return len(list(filter(lambda x: x== "x" or x== "X", list(txt)))) == len(list(filter(lambda x: x== "o" or x== "O", list(txt))))

print(XO("ooxx")) #True

print(XO("ooxXm") ) # True

print(XO("xooxx")) #False