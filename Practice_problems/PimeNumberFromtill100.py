
start= 1 
end = 100
for num in range(start,end+1):
    if num>1:
        for j in range(2,num):
            if num % j ==0:
                break
        else:
            print(num)
    