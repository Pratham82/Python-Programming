"""
Given an integer, , print its first  multiples. Each multiple  (where ) 
should be printed on a new line in the form: n x i = result.
"""


import math
import os
import random
import re
import sys


n = int(input("Enter value"))
if __name__ == '__main__':
    for i  in range(1,11):
        print("{0} x {1}: ".format(n,i),n*i)




