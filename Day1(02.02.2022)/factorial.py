n = int(input("Enter a number: "))

def fact(n):
	mult = 1
	while n>0:
		mult *= n
		n -= 1
	return mult

print(fact(n))



