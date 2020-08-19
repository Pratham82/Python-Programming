# Recursion: Sum
# Write a function that finds the sum of the first n natural numbers. Make your function recursive.

def sum_numbers(n):
    return n if n == 0 else sum_numbers(n - 1) + n


print(sum_numbers(12))
