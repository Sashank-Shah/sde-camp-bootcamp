cont = 'y'
while (cont == 'y') or (cont == 'Y'):
	num = int(input("Enter number: "))
	if num%2 == 0:
		print("even")
	else:
		print("odd")
	cont = input("continue checking? (y/n): ")


