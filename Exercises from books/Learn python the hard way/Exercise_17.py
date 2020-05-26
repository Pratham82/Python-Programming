from sys import argv 
from os.path import exists

script, in_file, out_file = argv

# Making object for reading though a file
ip_object = open(in_file)
ip_data = ip_object.read()

print(f"The input files is {len(ip_data)} bytes long")
print("Does the output file exist", exists(out_file))

# If we pass 'w' then it will overwrite the file and deletes old content
# If we pass 'a' then it will only append the text provided and keeps the old
# content as it is
out_obj = open(out_file,'a')

print("Do you want to continue this process if yes hit y or n for canceling ")
choice = input("Enter choice: ")
if choice == 'y':
    out_obj.write(ip_data) 
    print("Copy paste done")
elif choice  == 'n':
    print("Copy canceled")

