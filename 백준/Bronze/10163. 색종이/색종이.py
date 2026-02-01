import sys
input = sys.stdin.readline

N = int(input())

# init = []
# for _ in range(1001):
#     init.append([0] * 1001)

# 색종이 초기설정
paper = [[0] * 1001 for _ in range(1001)]


# 모든 색종이를 칠하기 -> 기존 색종이를 덮어씌우는게 포인트다.. 문제 안읽고 중첩으로 풀었네..
for k in range(1, N + 1):

    x, y, w, h = map(int, input().split())

    for i in range(x, x + w):
        for j in range(y, y + h):
            paper[i][j] = k

# 각 보이는 색종이 넓이 저장할 리스트
total = [0] * (N + 1)    

# 전체 색종이에 보이는 번호를 그 리스트 번호에 담는다
for i in range(1001):
    for j in range(1001):
        num = paper[i][j]
        if num > 0:
            total[num] += 1

for k in range(1, N + 1):
    print(total[k])