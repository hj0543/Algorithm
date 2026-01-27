import sys
sys.stdin = open('input.txt', 'r')

N = list(map(int, input().split())) 

sample = [1, 2, 3, 4, 5, 6, 7, 8]

if N == sample:
    print('ascending')
elif N == sample[::-1]:
    print('descending')
else:
    print('mixed')



