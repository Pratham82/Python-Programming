import subprocess as sp

string1 ="notepad file1"
l1 = string1.split()
filename = l1[0]+".exe"

print(filename)

code= "C:\Program Files\Microsoft VS Code\Code.exe"
file="file.txt"
sp.Popen(code, file)