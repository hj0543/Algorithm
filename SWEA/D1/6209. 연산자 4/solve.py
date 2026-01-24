import sys
sys.stdin = open('input.txt', 'r')

N = float(input())
num = "{:.2f}".format(N)
 
result = '{:.2f}'.format((N - 32) / 1.8)
print(f'{num} ℉ =>  {result} ℃')
