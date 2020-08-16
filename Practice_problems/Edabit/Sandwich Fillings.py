# Sandwich Fillings
# Given a sandwich (as a list), return a list of fillings inside the sandwich. This involves ignoring the first and last elements.

def get_fillings(sandwich):
	return sandwich[1:-1]


print(get_fillings(["bread", "ham", "cheese", "ham", "bread"]))