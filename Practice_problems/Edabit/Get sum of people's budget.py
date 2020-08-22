# Get Sum of People's Budget
# Create the function that takes a list of dictionaries and returns the sum of people's budgets.

# Examples
# get_budgets([
#   { "name": "John", "age": 21, "budget": 23000 },
#   { "name": "Steve",  "age": 32, "budget": 40000 },
#   { "name": "Martin",  "age": 16, "budget": 2700 }
# ]) ➞ 65700
import functools
def get_budgets(lst):
	# sum = lst[0]['budget']  # This will give us the value of key budget
	sum =0
	for i in range(len(lst)):
    		sum = sum + lst[i]['budget']
	return sum

print(get_budgets([
  { "name": "John",  "age": 21, "budget": 29000 },
  { "name": "Steve",  "age": 32, "budget": 32000 },
  { "name": "Martin",  "age": 16, "budget": 1600 }
]))