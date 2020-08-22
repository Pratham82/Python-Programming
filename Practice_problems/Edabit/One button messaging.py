# One Button Messaging Device
# Imagine a messaging device with only one button. For the letter A, you press the button one time, for E, you press it five times, for G, it's pressed seven times, etc, etc.

# Write a function that takes a string (the message) and returns the total number of times the button is pressed.
import functools
def how_many_times(msg):
	# return functools.reduce(lambda x, y: ord(x) + y, list(msg))
	# return list(lambda x: ord(x), list(msg))
	return ord(list(msg)[1])

print(how_many_times("abde"))

# soln
def how_many_times(msg):
		return sum([ord(x.lower())-96 for x in msg])