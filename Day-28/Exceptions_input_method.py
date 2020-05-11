def int_checker():
    while True:
        try:
            num = int(input("Enter number here: "))

        except:
            print("That doesn't look like a number")
        
        else:
            print("Correct number entered execution completed")
            break
        
        finally:
            print("try /except /finally block ")
            print("Try again to enter to correct number")

   
int_checker()

