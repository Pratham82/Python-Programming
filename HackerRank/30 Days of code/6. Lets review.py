"""
Given a string, , of length  that is indexed from  to , print its even-indexed 
and odd-indexed characters as  space-separated strings on a single line 

Sample Input
2
Hacker
Rank

Sample Output
Hce akr
Rn ak

"""

# Take the number of splits

N = int(input())

for i in range(0,N):
    string = input()
    for j in range(0,len(string)):
        if j % 2 == 0:
            print(string[j],end="")

    print(" " ,end ="")

    for k in range(0,len(string)):
        if k % 2 != 0:
            print(string[k],end="")
    

    print("")
