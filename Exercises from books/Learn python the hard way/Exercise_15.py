# Reading files
from sys import argv

# script, filename = argv
script,filename = input("Enter script name, file name: ").split(",")
prompt ="-->"

text = open(filename)

print(f"This is text file {filename} and its content:  ")
print(text.read())

# print(f"Type filename again")
file_new = input(prompt)

file_new = open(file_new)
print(file_new.read())