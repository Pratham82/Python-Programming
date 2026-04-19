List1 = [343,4545,56,6,78,789,989,789,0]

print("List1: ",List1)

# Methods for list

# The append() method adds an item to the end of the list.
List1.append(45)
print("List1: ",List1)

# The extend() extends the list by adding all items of a list (passed as an argument) to the end.
List2 =[111,122,1,33,44]
List1.extend(List2)

print("List1: ",List1)

# language list
language = ['French', 'English', 'German']

# language tuple
language_tuple = ('Spanish', 'Portuguese')

# language set
language_set = {'Chinese', 'Japanese'}

# Extending tuples and sets to a list
language.extend(language_set)
language.extend(language_tuple)
print("Language list: ",language)

# Wec can also add items to the list using add operators

a = [44,55,4,1,5]
b = [99,4,4,5,154]
a+=b
print("a: ",a)

# The insert() method inserts an element to the list at a given index.

List3 = [101,102,103,104,105]
List3.insert(1,111)
print(List3)

# The remove() method removes the first matching element (which is passed as an argument) from the list.

List3.remove(111)
print(List3)

# It does not removes duplicate elements in the list
List3 = [101,102,103,104,105,105,105]
List3.remove(105)
print(List3)

# The pop() method removes the item at the given index from the list and returns the removed item.
List4 = [111,112,113,114,115]
List4.pop(-2)
print(List4)

# The argument passed to the method is optional. If not passed, the default index -1 is passed as an argument (index of the last item).
List4.pop()
print(List4)

# The reverse() method reverses the elements of a given list.
#The reverse() function doesn't take any argument.
List4.reverse()
print(List4)

# The sort() method sorts the elements of a given list.

vowels = ['e', 'a', 'u', 'o', 'i']
vowels.sort()
print('Sorted list:', vowels)