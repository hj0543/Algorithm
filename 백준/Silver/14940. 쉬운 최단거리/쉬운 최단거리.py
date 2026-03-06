import sys
input = sys.stdin.readline
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(sr, sc):
    # 함수 내부에서 큐를 만들고 넘겨받은 시작점을 넣습니다.
    q = deque([(sr, sc)])

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < m:
                if maze[nr][nc] == 1 and visited[nr][nc] == -1:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))

n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, input().split())))

visited = [[-1] * m for _ in range(n)]
sr, sc = -1, -1

# 지도 전체를 돌며 초기화 작업 진행
for i in range(n):
    for j in range(m):
        if maze[i][j] == 2:
            sr, sc = i, j      # <--- q.append 대신 시작 좌표를 갱신해 줍니다!
            visited[i][j] = 0
        elif maze[i][j] == 0:
            visited[i][j] = 0

# 찾아낸 시작 좌표를 함수에 넘겨줍니다.
bfs(sr, sc)

for row in visited:
    print(*row)
