# Stand in Line
# Write a function that takes a list and a number as arguments. Add the number to the end of the list, then remove the first element of the list. The function should then return the updated list.
def next_in_line(lst, num):
	val = lst[1:]
	val.append(num)
	return val

print(next_in_line([5, 6, 7, 8, 9], 1))