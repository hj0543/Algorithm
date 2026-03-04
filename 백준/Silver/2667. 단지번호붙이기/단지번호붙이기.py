import sys
input = sys.stdin.readline

from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(sr ,sc):
    q = deque([(sr, sc)])
    grid[sr][sc] = 0
    counts = 1

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < n:
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 0
                    q.append((nr, nc))
                    counts += 1
    return counts

n = int(input())
grid = []
for _ in range(n):
    grid.append(list(map(int,input().rstrip())))

apt_counts = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            apt_counts.append(bfs(i, j))

apt_counts.sort()
print(len(apt_counts))
for count in apt_counts:
    print(count)
