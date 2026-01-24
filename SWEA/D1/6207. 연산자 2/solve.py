import sys
sys.stdin = open('input.txt', 'r')

N = float(input())
num = "{:.2f}".format(N)
 
result = '{:.2f}'.format(N * 2.2046)
print(f'{num} kg =>  {result} lb')
