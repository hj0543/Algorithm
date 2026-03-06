import sys
sys.stdin = open('input.txt', 'r')

##################################################
# 17086
import sys
input = sys.stdin.readline
from collections import deque

dr = [-1, 0, 1, 0, -1, 1, -1, 1]
dc = [0, 1, 0, -1, 1, 1, -1, -1]

def bfs(starts):
    q = deque(starts)

    for sr, sc in starts:
        visited[sr][sc] = 0

    while q:
        r, c = q.popleft()

        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < m:
                if grid[nr][nc] == 0 and visited[nr][nc] == -1:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))

n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

visited = [[-1] * m for _ in range(n)]

sharks = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            sharks.append((i, j))

bfs(sharks)

max_safety_length = 0
for i in range(n):
    if max_safety_length < max(visited[i]):
        max_safety_length = max(visited[i])

print(max_safety_length)