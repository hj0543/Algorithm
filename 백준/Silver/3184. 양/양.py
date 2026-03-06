import sys
input = sys.stdin.readline
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(sr, sc):
    q = deque([(sr, sc)])
    visited[sr][sc] = True
    sheep = 0
    wolf = 0

    if grid[sr][sc] == 'o':
        sheep += 1
    elif grid[sr][sc] == 'v':
        wolf += 1

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < R and 0 <= nc < C:
                if not visited[nr][nc] and grid[nr][nc] != '#':
                    visited[nr][nc] = True

                    if grid[nr][nc] == 'o':
                        sheep += 1
                    elif grid[nr][nc] == 'v':
                        wolf += 1
                    q.append((nr, nc))

    if wolf >= sheep:
        sheep = 0
    else:
        wolf = 0
    return wolf, sheep



R, C = map(int, input().split())
grid = []
for _ in range(R):
    grid.append(list(map(str, input().rstrip())))

visited = [[False] * C for _ in range(R)]

total_wolf = 0
total_sheep = 0

for i in range(R):
    for j in range(C):
        if grid[i][j] != '#' and not visited[i][j]:
            w, s = bfs(i, j)
            total_wolf += w
            total_sheep += s

print(total_sheep, total_wolf)