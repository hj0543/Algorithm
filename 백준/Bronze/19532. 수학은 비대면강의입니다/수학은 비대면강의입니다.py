import sys
input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())

# x 값 구하기
if a * e - d * b != 0:
    x = (c * e - f * b) // (a * e - d * b)

# y 값 구하기
if b != 0:
    y = (c - a * x) // b
else:
    y = (f - d * x) // e

print(x, y)