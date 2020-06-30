# Jaccard similarity

def jaccard_similarity(set_1, set_2):
    jac_sim = len(set_1.intersection(set_2)) / len(set_1.union(set_2))
    jac_distance = (1 - jac_sim) * 100
    jac_sim *= 100

    print(f'Set_1: {set_1}, \nSet_2: {set_2}')
    print(f"Jaccard similarity : {jac_sim}% ")
    print(f"Jaccard distance : {jac_distance}%\n")


set1 = {'dog', 'cat', 'cat', 'rat'}
set2 = {'dog', 'cat', 'mouse', 'butterfly'}
set3 = {0, 1, 2, 5, 6}
set4 = {0, 2, 3, 4, 5, 7, 9}

jaccard_similarity(set1, set2)
jaccard_similarity(set3, set4)
