val = False

while val == False :
    string = input("Enter your name: ")
    if not string:
        print("You didn't entered anything ")
        continue
    else:
        print(f"You entered {string}")
        val = True