num1 = int(input("Enter number: "))

def PrimeChecker(num1):
    if num1>1:
        for i in range(2,num1):
            if (num1 % i)==0:
                print(num1," not prime number")
                break
        else:
            print(num1," is a prime number")
    else:
        print(num1," is not prime number")

# Checking number using created function
PrimeChecker(num1)

