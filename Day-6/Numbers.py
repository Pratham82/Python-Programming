'''
Number data types store numeric values. They are immutable data types, means that changing the value of a number data type results in a newly allocated object.
Number objects are created when we assign value to variables.
'''

num1 = 45
num2 = 58

# del num1

print num1
# If we try to print the value of num1 then we will get following error
# NameError: name 'num1' is not defined

'''
Numerical types in python:
1. int (signed integers): They are often called just integers or ints, are positive or negative whole numbers with no decimal point.
2 long (long integers ): Also called longs, they are integers of unlimited size, written like integers and followed by an uppercase or lowercase L.
3. float (floating point real values): Also called floats, they represent real numbers and are written with a decimal point dividing the integer and fractional parts.
4. complex (complex numbers): are of the form a + bJ, where a and b are floats and J (or j) represents the square root of -1 (which is an imaginary number). The real part of the number is a, and the imaginary part is b. 
'''

num1 = 4545          # int
num2 = 4543424454L   # Long
num3 = 54.7          # float
num4 = 3.15j         # complex


print "num1: ", num1, type(num1)
print "num2: ", num2, type(num2)
print "num3: ", num3, type(num3)
print "num4: ", num4, type(num4)

'''
Number type conversion:
Python converts numbers internally in an expression containing mixed types to a common type for evaluation.
We can explicitly convert the number one type to another type by using type conversion

Type int(x) to convert x to a plain integer.
Type long(x) to convert x to a long integer.
Type float(x) to convert x to a floating-point number.
Type complex(x) to convert x to a complex number with real part x and imaginary part zero.
Type complex(x, y) to convert x and y to a complex number with real part x and imaginary part y. x and y are numeric expressions.
'''

print "\nType conversion: "

# Converting int to float

num1Float = float(num1)

print num1Float, type(num1Float) 

# Converting float to int

num3Int =int(num3)

print num3Int, type(num3Int)

numNew =454
# Converting int to complex number
numNewInt = complex(numNew)

print numNewInt, type(numNewInt)
