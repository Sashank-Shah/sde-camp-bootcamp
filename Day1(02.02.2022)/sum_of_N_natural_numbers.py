n = int(input("Enter the value of n: "))
def sum_n(n):
	sum = 0
	w = 1
	while w <= n:
		sum += w
		w += 1

	return sum

print(sum_n(n))