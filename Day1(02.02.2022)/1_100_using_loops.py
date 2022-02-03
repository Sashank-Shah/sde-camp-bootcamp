count = 1
print("for loop ")
for i in range(1, 101):
	if count < 10:
		print(i, end=" ")
		count += 1
	else:
		print(i)
		count = 1

print()
print("while loop ")
i = 0
while i<100:
	i += 1
	if count < 10:
		print(i, end=" ")
		count += 1
	else:
		print(i)
		count = 1

