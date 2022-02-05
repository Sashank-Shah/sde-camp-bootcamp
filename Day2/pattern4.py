'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 

'''

import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

def pat1(n):
	for row in range(1, n+1):
		for col in range(1, row+1):
			print(col, end=" ")
		print()



pat1(n=int(input()))