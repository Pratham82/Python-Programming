"""
Finding the percentage
Input:
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Output:
56.00
Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.1
"""
from functools import reduce
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    required_arr = student_marks[query_name]
    op = format(
        reduce(lambda a, b: a + b, required_arr) / len(required_arr), '.2f')
    print(op)
