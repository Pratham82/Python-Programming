# Jaccard similarity

def jaccard_similarity(list_1,list_2):
    set_1   = set(list_1)
    set_2   = set(list_2)
    jac_sim = len(set_1.intersection(set_2)) /len(set_1.union(set_2)) 
    jac_distance = (1 - jac_sim ) *100
    jac_sim *= 100

    print(f'Set_1: {set_1}, \nSet_2: {set_2}')
    print(f"Jaccard similarity : {jac_sim}% ")
    print(f"Jaccard distance : {jac_distance}%\n")
    
           
list1 = ['dog', 'cat', 'cat', 'rat']
list2 = ['dog', 'cat', 'mouse','butterfly']
list3 = [0,1,2,5,6]
list4 = [0,2,3,4,5,7,9]

jaccard_similarity(list1, list2)
jaccard_similarity(list3, list4)


    