# Get the square of only odd numbers and store it in a list

# nomral way
odd_sq = []
for i in range(23):
    if i % 2 ==1:
        odd_sq.append(i**2)

print(odd_sq)

# Using list comprehension

odd_sq_new = [i**2 for i in range(23) if i% 2==1]

print(odd_sq_new)
