# uke, I Am Your ...
# Luke Skywalker has family and friends. Help him remind them who is who. Given a string with a name, return the relation of that person to Luke.

# Person	Relation
# Darth Vader	father
# Leia	sister
# Han	brother in law
# R2D2	droid

def relation_to_luke(name):
	d1 = {"Darth Vader": "father", "Leia": "sister", "Han": "brother in law", "R2D2": "droid"}
	return f'Luke, I am your {d1[name]}'



print(relation_to_luke("Darth Vader") )