# Filter out Strings from an Array
# Create a function that takes a list of non-negative integers and strings and return a new list without the strings.


def filter_list(lst):
	return list(filter(lambda x: type(x) == int, lst))


print(filter_list([1, 2, "aasf", "1", "123", 123]))