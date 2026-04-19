f = open("Files/Legends.txt",mode="at",encoding="utf-8")
f.writelines(["\nNeymar Jr.","\nPele"])
f.close()

readFile= open("Files/Legends.txt",mode="rt",encoding="utf-8")
print("Content in legends:",readFile.read())