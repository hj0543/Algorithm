import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    print(A + B)
