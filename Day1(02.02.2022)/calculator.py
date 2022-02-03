num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
oper = input("press * / + - to use: ")

def calc(oper):
	switch = {
	'*': num1*num2,
	'/': num1//num2,
	'-': num1-num2,
	'+': num1+num2
	}

	return switch.get(oper, 'invalid operation')

print("{} {} {} = {}".format(num1, oper, num2, calc(oper)))