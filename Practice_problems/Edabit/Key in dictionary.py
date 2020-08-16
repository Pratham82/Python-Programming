# Does the Dictionary Contain a Given Key?
# Write a function that returns True if a dictionary contains the specified key, and False otherwise.

def has_key(dictionary, key):
	return key in dictionary


print(has_key({"craves": True, "midnight": True, "snack": True}, "morning"))

print(
has_key({ "pot": 1, "tot": 2, "not": 3 }, "not"))