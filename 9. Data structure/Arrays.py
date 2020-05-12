from array import * 

# making an integer array
val =array('i',[44,5,46,54,65,411,48,74,89,54])

# prints out address of array and size in order
print("Buffer info: ",val.buffer_info())

print("Typecode: ",val.typecode)

val.reverse()
print("After reverse: ",val)

# Iterating over array

for i in val:
    print(i,end=",")

# making a character array
# we have to use u keyword which signifies the unicode values

val2 = array('u',['a','d','i','d','a','s'])

print("\n\nval2: ")
for i in val2:
    print(i,end="")


# getting values form already created array

valCopy = array(val.typecode, (a for a in val))

# Iteration using for

print('\n\nvalCopy: ')
for i in valCopy:
    print(i,end=",")

# Iteration using while
i=0
while i<len(valCopy):
    print(valCopy[i])
    i+=1

