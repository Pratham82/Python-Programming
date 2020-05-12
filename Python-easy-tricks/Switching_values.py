# Switch values without using temp variable

num1 = 234
num2 = 344

print(f"num1: {num1}\nnum2: {num2}")
# Switch varibale directly

num1, num2 = num2,num1

print("Values after switching: ")

print(f"num1: {num1}\nnum2: {num2}")


