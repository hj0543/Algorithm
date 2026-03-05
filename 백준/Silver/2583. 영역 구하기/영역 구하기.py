import sys
input = sys.stdin.readline
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(sr, sc):
    q = deque([(sr, sc)])
    visited[sr][sc] = True
    area = 1

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < m and 0 <= nc < n:
                if grid[nr][nc] == 0 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr, nc))
                    area += 1
    return area

m, n, k = map(int, input().split())
grid = [[0] * n for _ in range(m)]

for i in range(k):
    c1, r1, c2, r2 = map(int, input().split())

    for j in range(r1, r2):
        for k in range(c1, c2):
            grid[j][k] = 1
# print(grid)

visited = [[0] * n for _ in range(m)]

counts = 0
total = []

for i in range(m):
    for j in range(n):
        if grid[i][j] == 0 and not visited[i][j]:
            total.append(bfs(i, j))
            counts += 1
result = sorted(total)

print(counts)
print(*result)