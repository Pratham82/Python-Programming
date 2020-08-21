# Recursion: Length of a String
# Write a function that returns the length of a string. Make your function recursive.

def length(txt):
	return 0 if len(txt) == 0 else 1 +  length(txt[1:]) 

print(length("apple"))