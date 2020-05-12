# Removing duplicate value from list

list1 = [22,34,55,43,64,55,76,22,45,45,22,56,76,88]

print(list1)

print("List after removing duplicates: ")

# Find a number which occured maximum time
list_max = max(set(list1), key = list1.count)

print("Number which occured the max time in list: ",(list_max))

# Removinfg duplicates using set 
list_no_dupl = list(set(list1))

print(list_no_dupl)
