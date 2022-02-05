'''

*********
 *******
  *****
   ***
    *


'''



import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

def pat1(n):
    for row in range(1, n+1):
        for col in range(1, n+1):
            if col <= row-1:
                print(" ",end="")
            else:
                print("*", end="")
        for col in range(n-row):
            print("*", end="")

        print()

pat1(n=int(input()))