# Nomral flow
def add(a,b):
    print(f"{a} + {b}: {a+b}")

add(12,34)

# Exception occured in a program

# Because strings and int cannot be added and this causes exception
# add(12,"34")   

# To handle this exception we will use try and except block 

# Using try, except and else block
def add(a,b):
    try:
        # print(f"{a} + {b}: {a+b}")
        result = a + b
    except:
        print("Looks like the inputs aren't correct please check the inputs again");
    else:
        print("Execution completed")
        print(f"{a} + {b}: {a+b}")


add(12,"234")



