import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

white = 0
blue = 0

def divide(x, y, size):
    global white, blue

    color = board[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if board[i][j] != color:
                half = size // 2
                divide(x, y, half)
                divide(x, y + half, half)
                divide(x + half, y, half)
                divide(x + half, y + half, half)
                return

    if color == 0:
        white += 1
    else:
        blue += 1

divide(0, 0, n)

print(white)
print(blue)