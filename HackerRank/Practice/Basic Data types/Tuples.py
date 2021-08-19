"""
Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of .
"""


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tuple1 = tuple(integer_list)
    print(hash(tuple1))
