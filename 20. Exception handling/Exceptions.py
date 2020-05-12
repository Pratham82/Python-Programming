"""Exception handling: mechanism for interrupting normal program flow and continuing in surrounding context
Key concepts:
1. Raising an exception
2. Handling an exception
3. Unhandled exception 
4. Exception object
""" 

Digit_map={'zero':'0',
            'one':'1',
            'two':'2',
            'three':'3',
            'four':'4',
            'five':'5',
            'six':'6',
            'seven':'7',
            'eight':'8',
            'nine':'9',
            }

import sys
def convert(s):
    """Convert a string to an integer """
    try:
        number=''
        for token in s:
            number += Digit_map[token]
        return int(number)  
    except (KeyError,TypeError) as e:                         # using as keyword   
        print(f"Conversion error: {e!r}",file=sys.stderr)     # Print error message         
        # return -1 # The raise keyword is used to raise an exception.
        raise     # instead of returning un-pythonic error we can simply emit our error mesasage and re-raise the  exception using raise keyword

from math import log
def string_log(s):
    v = convert(s)                # Call convert
    return log(v)                 # Compute natural log


# Testing program using print statements

print(convert("five six nine five".split()))

# This line will create an exception because the word ninety is not present in our dictionary
print(convert("\nfive six ninety five".split()))

# This line will cause type error because teh 
print(convert("9444"))


"""
Exceptions resulting from programmer errors:
1. Indentation error
2. SyntaxError
3. NameError

They are harder to catch

"""