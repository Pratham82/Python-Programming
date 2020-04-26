from math import sqrt
def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n % i==0:
            return False
    return True


from pprint import pp
print([x for x in range(101) if is_prime(x)])


prime_square_divisors ={x*x: (1,x,x*x) for x in range(20) if is_prime(x)}
pp(prime_square_divisors)
