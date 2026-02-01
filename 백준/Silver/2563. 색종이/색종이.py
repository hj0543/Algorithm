import sys
input = sys.stdin.readline

N = int(input())


# 종이 초기 설정
paper = [[0] * 100 for _ in range(100)]


for _ in range(N):
    x, y = map(int, input().split())

# 색종이 범위가 종이 전체의 범위를 넘어가지 않았다면 색종이 범위만큼 1을 더한다.
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            if 100> i >= 0 and 100 > j >= 0:
                paper[i][j] = 1

# 전체 범위에서 1의 개수를 구한다.
total = 0
for i in range(100):    
    for j in range(100):
        total += paper[i][j]

print(total)