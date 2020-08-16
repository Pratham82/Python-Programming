# Check if a List Contains a Given Number
# Write a function to check if a list contains a particular number.


def check(lst, el):
    # Method 1
    for i in lst:
        if i == el:
            return True
            break
    else:
        return False
    # Method 2
    # return el in lst


print(check([1, 1, 2, 1, 1, 4], 4))


lst = [4, 4, 4, 5, 5]
