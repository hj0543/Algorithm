import sys
input = sys.stdin.readline
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 섬 번호 부여
def island_marking(sr, sc, island_idx):
    q = deque([(sr, sc)])
    visited[sr][sc] = True
    grid[sr][sc] = island_idx

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            # m 대신 n 사용 (정사각형 맵)
            if 0 <= nr < n and 0 <= nc < n:
                if not visited[nr][nc] and grid[nr][nc] == 1:
                    visited[nr][nc] = True
                    grid[nr][nc] = island_idx
                    q.append((nr, nc))

# 최단 다리 건설하기
def find_shortest_bridge(island_idx):
    q = deque()
    # m 대신 n 사용
    dist = [[-1] * n for _ in range(n)]

    # 같은 땅이면 거리0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == island_idx:
                q.append((i, j))
                dist[i][j] = 0

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < n:
                if grid[nr][nc] == 0 and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

                # 땅 만났을 때
                elif grid[nr][nc] > 0 and grid[nr][nc] != island_idx:
                    # 현재까지 건설한 다리 길이가 최단 길이
                    return dist[r][c]

    return float('inf')


# 백준 2146번은 N 하나만 입력받습니다.
n = int(input()) 
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

visited = [[False] * n for _ in range(n)]

island_idx = 2
for i in range(n):
    for j in range(n):
        if not visited[i][j] and grid[i][j] == 1:
            island_marking(i, j, island_idx)
            island_idx += 1

# 각 섬마다 다른 섬으로 가는 최단 다리 길이를 구하고 최솟값 갱신
min_bridge = float('inf')
for i in range(2, island_idx):
    min_bridge = min(min_bridge, find_shortest_bridge(i))

print(min_bridge)