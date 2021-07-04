# Normal method
def find_even_odd(n):
    if n % 2 == 0:
        return 'Given number is even'
    else:
        return 'Given number is odd'

print(find_even_odd(23))
print(find_even_odd(26))
        
# Lambda exp
find_even_odd_lambda = lambda n: 'Given number is even' if n % 2 == 0 else 'Given number is odd'

print(find_even_odd_lambda(56))
print(find_even_odd_lambda(109))

