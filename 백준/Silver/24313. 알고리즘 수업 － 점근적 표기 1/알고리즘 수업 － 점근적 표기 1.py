import sys
input = sys.stdin.readline

x, y = map(int, input().split())
c = int(input())
n = int(input())

if n*x + y <= c * n and x <= c: # c의 기울기가 항상 같거나 더 커야함. 평행할 시 일치하기 때문에 같다가 성립하고 기울기가 더 커야지만 항상 더 크다를 만족시킬 수 있음
    print(1)
else:

    print(0)
