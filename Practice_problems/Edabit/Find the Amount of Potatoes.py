# Find the Amount of Potatoes
# Create a function to return the amount of potatoes there are in a string.

def potatoes(potato):
	# return list(potato)
	return int(len(list(filter((lambda x: x == 'o'), list(potato)))) /2)

print(potatoes("potatopotato"))#2