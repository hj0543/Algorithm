# 추천문제 - 물놀이를 가자
 
# [로직전략]
# 1. 물에서 땅을 찾자
# 1-1. BFS - W인 좌표 list -> 거리 출력
 
from collections import deque
 
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
 
def bfs(q):
 
    while q:
        r, c = q.popleft()
 
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
 
            if 0 <= nr < n and 0 <= nc < m:
                if visited[nr][nc] == -1 and grid[nr][nc] == 'L':
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))
 
    return visited
 
TC = int(input())
for tc in range(TC):
    n, m = map(int, input().split())
    grid = [list(map(str, input().rstrip())) for _ in range(n)]
 
    # 땅인 좌표
    waters = []
    visited = [[-1] * m for _ in range(n)]
    q = deque()
 
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'W':
                q.append((i, j))
                visited[i][j] = 0  # 물의 위치는 거리가 0
 
    bfs(q)
 
    result = 0
    for i in range(n):
        result += sum(visited[i])
 
    print(f'#{tc+1} {result}')