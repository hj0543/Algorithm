import sys
input = sys.stdin.readline

TC = int(input())

data = []   # [[55, 185], [58, 183], [88, 186], [60, 175], [46, 155]]

for i in range(TC):
    info = list(map(int, input().split()))
    data.append(info)

rank = [] # 순위를 담을 리스트

for i in range(TC): # 0번부터
    counts = 1
    for j in range(TC): # 모든 사람에 대해서 검사
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]: # 나보다 둘 다 큰 사람 있으면 카운트 + 1
            counts += 1
    rank.append(counts)

print(*rank)