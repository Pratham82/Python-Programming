# Edaaaaabit
# Write a function that takes an integer and returns a string with the given number of "a"s in Edabit.

def how_many_times(num):
	return 'Ed{0}bit'.format("a" * num)

print(how_many_times(5)) #Edaaaaabit
print(how_many_times(0))  #Edbit
