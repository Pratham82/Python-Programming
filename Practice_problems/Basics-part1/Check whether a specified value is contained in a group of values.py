l1 = [465,455,54,5665,654,867]

def Check(Group,num):
    for i in Group:
        if i == num:
            return True
    return False
            

# n = input("Enter the number if it present in the list: ")
print(Check(l1,867))

