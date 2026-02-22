import sys
sys.stdin = open('input.txt', 'r')

##################################################

board = [[0] * 102 for _ in range(102)]

N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    # 색종이 영역을 1로 표시
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            board[i][j] = 1

# 둘레 계산
total_length = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(1, 101):
    for j in range(1, 101):
        if board[i][j] == 1:
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]

                # 옆 칸이 0이라면 테두리
                if board[nx][ny] == 0:
                    total_length += 1

print(total_length)






