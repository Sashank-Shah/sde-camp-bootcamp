num1 = int(input("Num1: "))
num2 = int(input("Num2: "))
num3 = int(input("Num3: "))

if (num1 > num2) and (num2 > num3):
	print("{} is largest".format(num1))
elif (num2 > num1) and (num2 > num3):
	print("{} is largest".format(num2))
else:
	print("{} is largest".format(num3))