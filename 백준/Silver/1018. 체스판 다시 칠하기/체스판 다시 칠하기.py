import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = []

for i in range(N):
    line = list(input().rstrip())
    board.append(line)

size = 8

pattern1 = ['W', 'B', 'W', 'B' ,'W' ,'B' ,'W' ,'B']
pattern2 = ['B', 'W', 'B' ,'W' ,'B' ,'W' ,'B', 'W']

board1 = []
board2 = []

# 체스판 1 만들기
for i in range(size):
    if i % 2 != 0:
        board1.append(pattern1)
    else:
        board1.append(pattern2)

# 체스판 2 만들기
for i in range(size):
    if i % 2 != 0:
        board2.append(pattern2)
    else:
        board2.append(pattern1)

paint_list = [] # 색을 칠한 횟수

# board1 과 체스판 색 비교
for i in range(N - size + 1):
    for j in range(M - size + 1):
        paint = 0
        for m in range(size):
            for n in range(size):
                if board[i+m][j+n] != board1[m][n]:
                    paint += 1
        paint_list.append(paint)

# board2 와 체스판 색 비교
for i in range(N - size + 1):
    for j in range(M - size + 1):
        paint = 0
        for m in range(size):
            for n in range(size):
                if board[i+m][j+n] != board2[m][n]:
                    paint += 1
        paint_list.append(paint)

print(min(paint_list))