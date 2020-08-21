# Calculate Using String Operation
# Create a function that takes two numbers and a mathematical operator and returns the result.

def calculate(num1, num2, op):
	str1 = '{0} {1} {2}'.format(num1,op,num2)
	return eval(str1)

print(calculate(4, 9, "+"))


def bitAnd(n1, n2):
	val = int(n1 and n2)
	def decimalToBinary(num):
		if num > 1:
			decimalToBinary(num // 2)
		return num % 2
	return decimalToBinary(val)

print(bitAnd(6,23))