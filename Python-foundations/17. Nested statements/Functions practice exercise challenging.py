# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(list1):
    # First we will take a code list which consist our list of numbers i.e (007) and add one more element to it.
    required =[0,0,7,'a']
    # We will iterate through the given list
    for i in list1:
        # Then we will check if the number in the given list matches with required list 
        # Then pop that element from the required list
        if i == required[0]: 
            required.pop(0)

    # If all the elements in the required are popped off then the length of list will become 1
    # We will check if this condition becomes true or not
    return len(required) == 1


print(spy_game([1,2,4,0,0,7,5])) 



# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number¶

# My way:
def count_primes_(n):
    primes=[]
    for i in range(1,n):
        count =0
        for j in range(1,i+1):
            if i % j==0:
                count=count+1
        if count==2:
            primes.append(i)
    print(primes)
    return len(primes)

print("My solution:",count_primes_(100))

# Instructor's solution

def count_primes2(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:           # Check if x is prime if it is then break out of the loop
        for y in primes:      # use the primes list!
            if x%y == 0:
                x += 2
                break
        else:                 # if x is prime then append it to the list of primes
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

count_primes2(100)

# PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter¶
def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])

print_big('a')




