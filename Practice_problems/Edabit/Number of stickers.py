# Number of Stickers
# Given an n * n * n Rubik's cube, return the number of individual stickers that are needed to cover the whole cube.

def how_many_stickers(n):
	return n * 6 if n == 1 else n ** 2 * 6


print(how_many_stickers(2)) #24
