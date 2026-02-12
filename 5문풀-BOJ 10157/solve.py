import sys
sys.stdin = open('input.txt', 'r')

##################################################

C, R = map(int, input().split())    # 7 6
K = int(input())                    # 11

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

grid = []
for i in range(R):
    grid.append([1] * C)

i, j = 0, 0
k = 0
while grid[i][j] <= C * R:

    if grid[i][j] += 1



print(grid)





