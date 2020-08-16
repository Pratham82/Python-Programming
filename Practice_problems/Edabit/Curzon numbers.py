# Curzon Numbers
# In this challenge, establish if a given integer num is a Curzon number. If 1 plus 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a Curzon number.

# Given a non-negative integer num, implement a function that returns True if num is a Curzon number, or False otherwise.

# Examples
# is_curzon(5) ➞ True
# # 2 ** 5 + 1 = 33
# # 2 * 5 + 1 = 11
# # 33 is a multiple of 11

def is_curzon(num):
	#  % 1+ 2 * num ==0
	n1 = 1 + (2 ** num)
	n2 =(2 *num) +1 
	return n1%n2 ==0

print(is_curzon(5))
362880
387420489