# Code run time is sometimes very crucial because one part of program can affect 
# whole program to slow down so in that case we can use timit module. With timit
# we can track the amount of time that code takes to run.

import timeit

# doing 1 task with different methods

'0-1-2-3-.....99'

# Tracking the execution time
# In the parenethisis 1st argument is your program code and next is no. of times 
# the execution
t1= timeit.timeit('a = "-".join(str(n) for n in range(100))',number =10000)
t2= timeit.timeit('a = "-".join([str(n) for n in range(100)])',number =10000)
t3= timeit.timeit('a = "-".join(map(str,range(100)))',number =10000)
print("Using normal joining:",t1)
print("Using list comp.:",t2)
print("Using map:",t3)

print(timeit.timeit(lambda: "-".join(map(str, range(100))), number=10000))
