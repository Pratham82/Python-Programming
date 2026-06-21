"""
- Create a variable grade holding an integer between 0 - 100

- Code if, elif, else statements to print the letter grade of the number grade variable

Grades:
A = 90 - 100
B = 80 - 89
C = 70-79
D = 60 - 69
F = 0 - 59


Example:
if grade = 87 then print('B')
"""

marks = 50


def getGrades(marks) -> str:
    grade = None
    if marks >= 90:
        grade = "A"
    elif 80 <= marks <= 89:
        grade = "B"
    elif 70 <= marks <= 79:
        grade = "C"
    elif 60 <= marks <= 69:
        grade = "D"
    elif 0 <= marks <= 59:
        grade = "F"
    return grade


print(getGrades(60))
