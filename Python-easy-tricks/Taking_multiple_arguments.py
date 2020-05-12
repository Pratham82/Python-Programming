# Taking multiple arguments in a method using args

def add(*a):
    res = 0
    for i in a:
        res += i
    return res

print(add(324,34,435,345,56,756788))
