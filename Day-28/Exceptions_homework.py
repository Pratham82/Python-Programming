# Problem 1 

for i in ['a','b','c']:
    try:
        print(i**2)
    except:
        print("Strings cannot be multiplied")
        break

# Problem 2
 
x = 5
y =0

try:
    z = x/y
except:
    print("Zero division error occurred change the denominator")
finally:
    print("All Done.")


# Problem 3

def ask():
    while True:     
        try:
            s = int(input("Input an integer: "))

        except:
            print("Incorrect input entered")

        else:
            print(f"Square of entered number: {s**2}")
            break

        finally:
            print("try/ expect/ else block executed")
            print("Enter correct input for getting the output")

ask()

print("__Instructors mehtod__")     
# Instructors way
def ask():
    waiting =True
    while waiting:     
        try:
            s = int(input("Input an integer: "))

        except:
            print("Incorrect input entered")
            continue
        else:
            waiting =False
    
    print(f"Square of entered number: {s**2}")
        

ask()
        
    