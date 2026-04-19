# Level 2 questions
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
# My answer
def has_33(list1):
    for i in range(0,len(list1)-1):
        for j in range(0,len(list1)-1,2):
            if list1[i]==3 and list1[j]==3:
                return True
            else:
                 pass

l1=[45,45,1,12,4,3,3,4]

print(has_33(l1))

# Instructor's answer

def has_33_n(list2):
    for i in range(0,len(list2)-1):
        # if list2[i]==3 and list2[i+1]==3:
        #Shorter wey:
        if list2[i:i+2]==[3,3]:
            return True 

print(has_33_n([87,4,4587,3,3,4,6]))

# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
#My answer
def paper_doll(txt):
    txt2=''
    for i in txt:
        txt2= txt2+i*3
    return txt2

print(paper_doll("hellow"))


# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# My answer: 
def blackjack(n,m,p):
    if sum((n,p,m)) <= 21:
        return sum((n,p,m))
    elif sum((n,p,m)) <=31  and 11 in (n,p,m):
        return sum((n,p,m))-10
    else:
        return "BUST"

print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))

# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers
# Instructor's answer 
def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total

print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))