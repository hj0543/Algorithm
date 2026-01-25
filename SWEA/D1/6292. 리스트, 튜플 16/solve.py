import sys
sys.stdin = open('input.txt', 'r')

N = list(map(int, input().split(',')))

print(list(N), tuple(N), sep = '\n')


    