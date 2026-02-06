import sys
input = sys.stdin.readline

N, K = map(int, input().split())

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def comb(n, r):
    result = factorial(n) / (factorial(n - r) * factorial(r))
    return result
if 0 <= K <= N:
    result = int(comb(N, K))
else:
    result = 0

print(result)