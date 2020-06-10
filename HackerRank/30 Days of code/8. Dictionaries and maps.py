# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

List_of_contacts =[]

for i in sys.stdin:
    List_of_contacts.append(i)

# Storing the first value that is number of entries
n = int(List_of_contacts[0])

# For storing the values from 1 to 3 in list
entries = List_of_contacts[1:n+1]

# For storing the values from 3 to end in list
queries = List_of_contacts[n+1:]

phoneBook ={}

# Now we will split the list of entries 
for i in entries:
    name, number = i.split()
    phoneBook[name] = number

for q in queries:
    StrippedQuery = q.rstrip()
    if StrippedQuery in phoneBook:
        print(StrippedQuery+"="+str(phoneBook[StrippedQuery]))
    else:
        print("Not found")


"""
Input: 
3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry
"""