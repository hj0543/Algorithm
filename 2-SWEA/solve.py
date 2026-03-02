import sys
sys.stdin = open('input.txt', 'r')

##################################################
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(sr, sc):
    q = deque([(sr, sc)])

    while q:
        r, c = q.popleft()

        if maze[r][c] == 3:
            return True

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < 100 and 0 <= nc < 100:
                if maze[nr][nc] != 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr, nc))

for _ in range(10):
    tc = int(input())
    maze = []
    for _ in range(100):
        maze.append(list(map(int, input().rstrip())))

    visited = [[False] * 100 for _ in range(100)]

    sr, sc = 0, 0
    for i in range(100):
        for j in range(100):
            if maze[i][j] == 2:
                sr, sc = i, j

    visited[sr][sc] = True

    if bfs(sr, sc):
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
