'''

* 
* * 
* * * 
* * * * 
* * * * * 

'''


import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

def pat1(n):
	for row in range(1, n+1):
		for col in range(row):
			print('*', end=" ")
		print()



pat1(n=int(input()))