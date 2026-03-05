import sys
input = sys.stdin.readline
from collections import deque

dr = [-2, -1, 1, 2, 1, 2, -2, -1]
dc = [1, 2, 2, 1, -2, -1, -1, -2]

def bfs(sr, sc):
    q = deque([(sr, sc)])
    visited[sr][sc] = 0

    while q:
        r, c = q.popleft()

        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < L and 0 <= nc < L:
                if visited[nr][nc] == -1:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))

TC = int(input())
for tc in range(TC):
    L = int(input())
    curr_r, curr_c = map(int, input().split())
    move_r, move_c = map(int, input().split())

    visited = [[-1] * L for _ in range(L)]
    bfs(curr_r, curr_c)
    # print(visited)

    print(visited[move_r][move_c])