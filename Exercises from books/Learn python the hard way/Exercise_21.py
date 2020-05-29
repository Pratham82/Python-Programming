def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a /b

print("Doing math with just the functions: ")

age = add(10,30)
height = subtract(78,10)
weight = multiply(2,100)
iq = divide(100,2)

print(f"Age: {age} years, Height: {height}in, Weight: {weight}lbs, IQ: {iq}")

what = add(age, subtract(height,multiply(weight,divide(iq,2))))

print(f"That becomes {what}, can you do it by hand?.")


