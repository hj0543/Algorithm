import sys
sys.stdin = open('input.txt', 'r')

N = float(input())
num = "{:.2f}".format(N)
 
result = '{:.2f}'.format(N * 1.8 + 32)
print(f'{num} ℃ =>  {result} ℉')
