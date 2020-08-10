def sortWithOut(data_list):
    newList = []
    while data_list:
        minimum = data_list[0]  # arbitrary number in list 
        for x in data_list: 
            if x < minimum:
                minimum = x
        newList.append(minimum)
        data_list.remove(minimum) 
    
    print (newList)


numbers = [12, 45, 8, 5, 71, 5, 41]
print(sortWithOut(numbers))
