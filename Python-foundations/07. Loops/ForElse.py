# Finding a number in the list which is divisible by 2

l1 =[45,78,41,56,42,91]
l1 =[45,73,41,51,49,91]


for i in l1:
    if i % 2 ==0:
        print(i)
        break;
    
else:
    print("Not found")

 # This else block will be printed multiple times
 # So rather using else block with if we can use else with our for loop
 # In certain condition where there is no number which is divisible by 2 this can be used