num =int(input("Enter number to get its table: "))

for i in range(1,11):
    # print(num ,"x",i,"=",num*i)
    print(num*i)


# Get a table from 11 to 30
print("Tables from 11 to 30")
for i in range(11,31):
    for j in range(1,11):
        # print(num ,"x",i,"=",num*i)
        print(j*i)