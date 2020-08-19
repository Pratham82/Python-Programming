# Where is Bob!?!
# Write a function that searches a list of names (unsorted) for the name "Bob" and returns the location in the list. If Bob is not in the array, return -1.

# Examples
# find_bob(["Jimmy", "Layla", "Bob"]) ➞ 2

def find_bob(names):
	return  names.index("Bob") if "Bob" in names else -1

print(find_bob(["Jimmy", "Layla", "Boba"]))