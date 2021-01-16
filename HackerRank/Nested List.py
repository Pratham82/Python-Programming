"""
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Example

The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:

 Sample Input 0
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output 0
Berry
Harry
"""
if __name__ == "__main__":
    score_list = {}

    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_list[name] = score

    second_highest = sorted(list(set(score_list.values())))[1]

    soln = []
    for x, y in score_list.items():
        if y == second_highest:
            soln.append(x)

    # print(sorted(soln))
    list(map(lambda x: print(x), sorted(soln)))
