

print(any([False,True,False]))

print(all([False,True,False]))


a = [324,45,54,6456,678,878,6]
b = [354,234,354,568,786,845,55]
for i in zip(a,b):
    print(i)

# Using tuple unpacking
for a,b in zip(a,b):
    print("Average: ",(a+b) / 2)


