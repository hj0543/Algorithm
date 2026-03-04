import sys
input = sys.stdin.readline
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(queue):

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < m:
                if box[nr][nc] == 0 and visited[nr][nc] == -2:
                    visited[nr][nc] = visited[r][c] + 1
                    box[nr][nc] = 1
                    queue.append((nr, nc))
    return False

m, n = map(int, input().split())
box = []
for _ in range(n):
    box.append(list(map(int, input().split())))

visited = [[-2] * m for _ in range(n)]

queue = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            visited[i][j] = 0
            queue.append((i, j))
bfs(queue)

for i in range(n):
    for j in range(m):
        if box[i][j] == -1 and visited[i][j] == -2:
            visited[i][j] = -1

max_day = 0
for i in range(n):
    for j in range(m):
        if max_day < max(visited[i]):
            max_day = max(visited[i])

for i in range(n):
    for j in range(m):
        if visited[i][j] == -2:
            print(-1)
            exit()

print(max_day)