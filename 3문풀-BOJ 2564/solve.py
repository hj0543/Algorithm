import sys
sys.stdin = open('input.txt', 'r')

##################################################

# 1 : 북 / 2 : 남 / 3 : 서 / 4 : 동

w, h = map(int, input().split())
N = int(input())

markets = []
for i in range(N):
    markets.append(list(map(int, input().split())))
d, p = map(int, input().split())

dist = 0

for i in range(N):
    # 동근이가 북쪽에 있을 때
    if d == 1:
        # 상점이 서쪽일 때
        if markets[i][0] == 3:
            dist += p + markets[i][1]
        # 상점이 동쪽일 때
        elif markets[i][0] == 4:
            dist += (w - p) + markets[i][1]
        # 상점이 북쪽일 때
        elif markets[i][0] == 1:
            dist += abs(p - markets[i][1])
        # 상점이 남쪽일 때
        else:
            if p + markets[i][1] <= w:
                dist += p + markets[i][1] + h
            else:
                dist += (2 * w) - (p + markets[i][1]) + h

    # 동근이가 남쪽에 있을 때
    if d == 2:
        # 상점이 서쪽일 때
        if markets[i][0] == 3:
            dist += p + (h - markets[i][1])
        # 상점이 동쪽일 때
        elif markets[i][0] == 4:
            dist += w - p + (h - markets[i][1])
        # 상점이 북쪽일 때
        elif markets[i][0] == 1:
            if p + markets[i][1] <= w:
                dist += p + markets[i][1] + h
            else:
                dist += (2 * w) - (p + markets[i][1]) + h
        # 상점이 남쪽일 때
        else:
            dist += abs(p - markets[i][1])

    # 동근이가 서쪽에 있을 때
    if d == 3:
        # 상점이 서쪽일 때
        if markets[i][0] == 3:
            dist += abs(p - markets[i][1])
        # 상점이 동쪽일 때
        elif markets[i][0] == 4:
            if p + markets[i][1] <= h:
                dist += p + markets[i][1] + w
            else:
                dist += (2 * h) - (p + markets[i][1]) + w
        # 상점이 북쪽일 때
        elif markets[i][0] == 1:
            dist += p + markets[i][1]
        # 상점이 남쪽일 때
        else:
            dist += (h - p) + markets[i][1]


    # 동근이가 동쪽에 있을 때
    if d == 4:
        # 상점이 서쪽일 때
        if markets[i][0] == 3:
            if p + markets[i][1] <= h:
                dist += p + markets[i][1] + w
            else:
                dist += (2 * h) - (p + markets[i][1]) + w
        # 상점이 동쪽일 때
        elif markets[i][0] == 4:
            dist += abs(p - markets[i][1])
        # 상점이 북쪽일 때
        elif markets[i][0] == 1:
            dist += p + (w - markets[i][1])
        # 상점이 남쪽일 때
        else:
            dist += (h - p) + (w - markets[i][1])

print(dist)
