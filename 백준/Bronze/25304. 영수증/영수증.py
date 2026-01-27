X = int(input())
N = int(input())

add = 0

for i in range(N):
    a, b = map(int, input().split())
    add += a * b

if X == add:
    print('Yes')
else:
    print('No')