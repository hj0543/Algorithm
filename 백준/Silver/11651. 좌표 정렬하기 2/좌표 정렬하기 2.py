import sys
input = sys.stdin.readline

TC = int(input())

data = []
for tc in range(1, TC + 1):
    data.append(list(map(int, input().split())))

data.sort(key=lambda x: (x[1], x[0]))

for i in range(len(data)):
    print(*data[i])