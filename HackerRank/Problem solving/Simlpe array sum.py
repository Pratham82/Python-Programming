def simpleArraySum(n, ar):
    #
    # Write your code here.
    sum = 0
    ar = ar.split(' ')
    for i in ar:
        sum += i

    return sum


print(simpleArraySum('6 1 2 3 4 10 1'))