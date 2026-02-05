import sys
sys.stdin = open('input.txt', 'r')

# 2839
import sys
input = sys.stdin.readline

N = int(input())

for x in range(N//3):
    for y in range(N//5):
        if 3*x + 5*y != N:
            print(-1)
            exit()
        else:
