# Characters in Shapes
# Create a function that counts how many characters make up a rectangular shape. You will be given a list of strings.

def count_characters(lst):
	return len(sum(list(map(lambda x: list(x), lst)),[]))


print(count_characters([
  "###",
  "###",
  "###"
]))