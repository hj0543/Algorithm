import sys
sys.stdin = open('input.txt', 'r')

# 과제풀이용
import sys
input = sys.stdin.readline


def fibo(n):
    a = 1
    b = 1
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    for i in range(1, n):
        a, b = b, b + a

    return a

N = int(input())

print(fibo(N))


