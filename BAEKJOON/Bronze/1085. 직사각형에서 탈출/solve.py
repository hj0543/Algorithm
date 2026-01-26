import sys
sys.stdin = open('input.txt', 'r')

x, y, w, h = map(int, input().split())
# [653, 375, 1000, 1000]

result = min(x, y, w - x, h - y)

print(result)





