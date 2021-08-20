import math
import os
import random
import re
import sys

if __name__ == '__main__':
    string_dict = {}
    s = input()
    # Adding the values in dictionary
    for i in sorted(list(s)):
      if i in string_dict:
        string_dict[i] += 1
      else:
        string_dict[i] = 1

    # Sorting the dictionary based on the values of the keys
    final_dict = dict(sorted(string_dict.items(), key=lambda item: item[1],reverse = True))

    # Creating an array for easy iteration
    dict_arr = list(final_dict.items())

    # Iterating over most occurred 3 values
    for i in range(0, 3):
      print(f'{dict_arr[i][0]} {dict_arr[i][1]}')
