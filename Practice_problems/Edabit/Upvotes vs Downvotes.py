# Upvotes vs Downvotes
# Given a dictionary containing counts of both upvotes and downvotes, return what vote count should be displayed. This is calculated by subtracting the number of downvotes from upvotes.
from functools import reduce
def get_vote_count(votes):
	return votes['upvotes'] - votes['downvotes']

print(get_vote_count({ "upvotes": 13, "downvotes": 0 }))


print(get_vote_count({ "upvotes": 2, "downvotes": 33 }))


print(get_vote_count({'downvotes': 4, 'upvotes': 1}))







dictionary1 = {"upvotes": 13, "downvotes": 0}

# this will iterate over keys
for i in dictionary1:
	print(i)

print('----')
print(dictionary1['upvotes'])

# this will iterate over items
for v in dictionary1.items():
	print(v)

l1 = list(dictionary1.values())

print(l1)