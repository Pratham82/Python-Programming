from sys  import argv
from os.path import exists

script, in_file, out_file = argv

# Creating file object 
in_file_obj = open(in_file)
input_text = in_file_obj.read()

dec = input("Do you want to copy paste file?, enter 'y' or 'n': ")
if dec =='y':
    out_file_obj = open(out_file,'w')
    out_file_obj.write(input_text)
    print("Copy pasting done")
elif dec =='n':
    print("Copy pasting canceled")
