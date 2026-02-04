import sys
sys.stdin = open('input.txt', 'r')

# 1629
import sys
input = sys.stdin.readline

N = int(input())

def my_abs(a, b):
    if a - b == - b:
        result = 0
    elif a - b >= 0:
        result = a - b
    else:
        result = b - a
    return result

for _ in range(N):
    T = int(input())
    board = [list(map(int, input().split())) for _ in range(T)]

    # 0으로 채워진 7 x 7 행렬 생성
    grid = [[0] * 7 for _ in range(7)]

    # 0으로 채워진 7 x 7 행렬에 불러온 행렬을 모서리를 비워둔채로 삽입
    for i in range(5):
        for j in range(5):
            grid[i+1][j+1] = board[i][j]

    total = 0
    for i in range(1, T+1):
        for j in range(1, T+1):
            a = my_abs(grid[i][j+1], grid[i][j])
            b = my_abs(grid[i-1][j], grid[i][j])
            c = my_abs(grid[i+1][j], grid[i][j])
            d = my_abs(grid[i][j-1], grid[i][j])
            add = a + b + c + d
            total += add
    print(f'#{_+1} {total}')


