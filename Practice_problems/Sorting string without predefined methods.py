def reversignString(str):
    strNew = ""
    j = len(str) -1
    print(j)
    
    for i in str:
        strNew = i + strNew
        

    return strNew
    


print(reversignString("FORD"))