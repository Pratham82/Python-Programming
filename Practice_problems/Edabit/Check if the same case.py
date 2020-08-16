# Check if the Same Case
# Create a function that returns True if an input string contains only uppercase or only lowercase letters.

def same_case(txt):
	# return list(map(lambda c,: c ==  , list(txt)) )
	lst = list(txt)
	lstCheck =[]
	for i in range(len(txt)):
		lstCheck.append(lst[i].isupper() == lst[0].isupper())

	return all(lstCheck)

print(same_case("HELLO"))
