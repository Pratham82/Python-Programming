import subprocess as sp


program_name ="Code.exe"
# file_name = "file.txt"
# We can pass file name as an input or decare default filename 
file_name = input("Filename: ")
sp.Popen([program_name,file_name])



