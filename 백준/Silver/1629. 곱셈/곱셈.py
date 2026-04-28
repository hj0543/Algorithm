import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def power(a, b):
    if b == 1:
        return a % C

    half = power(a, b // 2)

    if b % 2 == 0:
        return (half * half) % C
    else:
        return (half * half * a) % C

print(power(A, B))