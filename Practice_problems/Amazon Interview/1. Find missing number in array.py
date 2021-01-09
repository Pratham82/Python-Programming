# Find the missing number in the array
#
# You are given an array of positive numbers from 1 to n, such that all numbers from 1 to n are present except one number x. You have to find x. The input array is not sorted. Look at the below array and give it a try before checking the solution.


def find_missing(input_list):
    return sum([i for i in range(1, sorted(input_list)[-1] + 1)]) - sum(input_list)


print(find_missing([3, 7, 1, 2, 8, 4, 5]))
