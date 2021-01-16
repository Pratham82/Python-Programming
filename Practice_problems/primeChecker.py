# Prime number checker


def primeChecker():
    print("Enter the number for finding out if it's prime or not: ")
    n = int(input())

    check = [x for x in range(1, n + 1) if n % x == 0]
    print(f"{n} is a prime number") if len(check) == 2 else print(
        f"{n} is a not a prime number"
    )


primeChecker()
