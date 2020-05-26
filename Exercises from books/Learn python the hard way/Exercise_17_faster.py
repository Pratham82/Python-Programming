open("file2.txt",'a').writelines([l for l in open('file1.txt','r')])
print("Copy pasting done.")

