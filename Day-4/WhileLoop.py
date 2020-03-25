
# While loop will run until the specified condition is true
i = 1
while i < 5:
    print (i)
    i+=1

print
# With the break statement we can stop the loop even if the while condition is true:
i = 1
while i < 5:
    print(i)
    if i == 3:
        break
    i += 1


# With the continue statement we can stop the current iteration, and continue with the next:
print
i = 0
while i < 5:
    i += 1
    if i == 2:  # Here 3 will be skipped
        continue
    print(i)


# With the else statement we can run a block of code once when the condition no longer is true:
print
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")