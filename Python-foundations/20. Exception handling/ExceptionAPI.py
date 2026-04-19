# Exception form an important aspect of a API of function
# Callers of the function should know what type of exceptions are expected while calling an API

'''
Compute square roots using the method of Heron alexander
args:
    x: The number for which the squareroot is to be computed

Returns:
    The square root of x
'''
def square_root(x):
    if x < 0:
        raise ValueError(
        print(f"Cannot compute square root of a negative number {x}")
    )
    guess = x
    i = 0
    try:
        while guess * guess != x and i < 20:
            guess = (guess + x/ guess)/2.0
            i += 1
    except ZeroDivisionError:
        return ValueError()
    return guess

import sys
def main():
    try:
        print(square_root(9))
        print(square_root(2))
        print(square_root(-1))
        print("This is never printed")
    except ValueError as e:
        print(e,file=sys.stderr)
    
    print("Program execution continues, normally her")

if __name__ =='__main__':
    main()

'''
Use standard exception type errors
1. Standard types: Python provides standard exception types for signalling errors
2. Invalid argument: Use ValueError for argument of the right type but with an invalid value
3. Exception constructors: Use raise ValueError() to raise a new ValueError
'''