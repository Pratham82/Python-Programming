# Count Instances of a Character in a String
# Create a function that takes two strings as arguments and returns the number of times the first string (the single character) is found in the second string.
# char_count("a", "edabit") ➞ 1

def char_count(txt1, txt2):
	return len(list(filter(lambda v: v == txt1, list(txt2))))


print(char_count("c", "Chamber of secrets"))