
# While loop will run until the specified condition is true
i = 1
while i < 5:
    print i
    i += 1


# Using break statement we can stop the flow of the loop
print
i =1
while i < 5:
    print i
    if i == 3:      # Our loop will stop executing from 3
        break
    i += 1

# Example 2


# Continue: this wll skip the current iteration of loop and go to the next iteration

print "\nContinue Statement"
i =0
while i < 5:
    i += 1
    if i ==3:
        continue
    print (i)


print
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

print"\nElse Statement"
print
i =0
while i < 5:
    print i 
    i += 1
else:
    print("is no longer lesser than 5")

# Single Statement Suites

# Similar to the if statement syntax, if your while clause consists only of a single statement, it may be placed on the same line as the while header.

# infinite Loop
flag  =1 
# while flag: print "Flag is true"
print "End of while statement"
# Use CTL + C to end loop

