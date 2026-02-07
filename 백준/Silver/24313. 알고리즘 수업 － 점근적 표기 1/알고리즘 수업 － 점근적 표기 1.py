import sys
input = sys.stdin.readline

x, y = map(int, input().split())
c = int(input())
n = int(input())

if n*x + y <= c * n and x <= c:
    print(1)
else:
    print(0)