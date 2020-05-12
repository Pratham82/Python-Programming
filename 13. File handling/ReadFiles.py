f = open("Files/Test.txt", mode="rt",encoding="utf-8")
g = open("Files/fil1.txt", mode="rt",encoding="utf-8")
h = open("Files/wasteland.txt", mode="rt",encoding="utf-8")
# return type of read() method is str

# To read specific number of character we have to pass the characters as arguments
# print(f.read(25))

# To read the whole file we have to keep the argument of read() method empty
print("Content in Test1.txt:\n",f.read())
print()
print("Content in fil1.txt:\n",g.read())
print()
print("Content in wasteland.txt:\n",h.read())