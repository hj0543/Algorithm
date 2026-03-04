import sys
sys.stdin = open('input.txt', 'r')

##################################################
# 2667
import sys
input = sys.stdin.readline

from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(sr ,sc):
    q = deque([(sr, sc)])
    counts = 0
    while q:
        r, c = q.popleft()
        grid[r][c] = 0

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if grid[nr][nc] != 0:
                    grid[nr][nc] = 0
                    counts += 1
    return counts

n = int(input())
grid = []
for _ in range(n):
    grid.append(list(map(int,input().rstrip())))

apt = 0
houses = []
for i in range(n):
    for j in range(n):
        if grid[i][j] != 0:
            houses.append(bfs(i, j))
            apt += 1

print(apt)
for i in range(apt):
    print(houses)