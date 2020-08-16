def allCaps(str):
	return "".join(list(map((lambda c: c.capitalize()), list(str))))

print(allCaps('dsfgdgfg'))  # DSFGDGFG

def removeNewLines(str):
	word = ''
	for c in str:
		if c != '\n' and c!= '\r':
			word = word+ c
	return word
		
	
	# return (list(filter((lambda v: v != '\n'), str)))

print(removeNewLines('''
dfdfdf

dfdsfdgdfh

fghgfhgh
''' ))

def removeExtraSpace(str):
	# return "".join(list(map(lambda x: x != '  ', list(str))))
	return " ".join(str.split())

print(removeExtraSpace("ddf    fdfdf  ff fd fd f dffdf     dfdffd     df"))

def charCount(str):
	return len("".join(list(filter((lambda v: v != ' '), list(str)))))

print(charCount(' 1 2 3 4 5  6 7   8 9     10   111 '))