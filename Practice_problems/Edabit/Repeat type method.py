# Burrrrrrrp
# Create a function that returns the string "Burp" with the amount of "r's" determined by the input parameters of the function.

def long_burp(num):
    return 'Bu{0}p'.format('r' * num)



print(
long_burp(5) )