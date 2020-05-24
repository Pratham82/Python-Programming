from sys import argv
import sys

script, filename = argv
val = False
prompt ="-->"

# Creating file objects for writing and reading
file_obj_read = open(filename)
print("_________________________________")
print("This is old content in your file")
print(file_obj_read.read())
print("_________________________________")

file_obj =  open(filename,'w')


print(f"In order to write new text we have to erase {filename} file")

print("Do you want to continue?: enter 'y' ")


while val == False :
    decision = input(prompt)
    if not decision or decision!= 'y':
        print("You didn't entered anything / you didn't entered correct input ")
        decision = input(prompt)
        pass
    elif decision =='y':
        print("Opening file...")
        # Erasing file
        print(f"No we are deleting file")
        print("Are you sure: ?")
        file_obj.truncate()
        print("Files deleted")
        # Taking input for new lines
        print("Enter new text: ")
        line1 = input(prompt)

        
        # Adding our new lines to the file
        file_obj.write(line1)
        print("Lines added")
        file_obj.close()
        val =  True



