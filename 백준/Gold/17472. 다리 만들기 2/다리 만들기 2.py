import sys
input = sys.stdin.readline
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


# 1. 섬 번호 부여
def island_marking(sr, sc, island_idx):
    q = deque([(sr, sc)])
    visited[sr][sc] = True
    grid[sr][sc] = island_idx

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if not visited[nr][nc] and grid[nr][nc] == 1:
                    visited[nr][nc] = True
                    grid[nr][nc] = island_idx
                    q.append((nr, nc))


def bridges():
    edges = []
    for r in range(n):
        for c in range(m):
            if grid[r][c] >= 2:  # 섬에서 출발
                curr_island = grid[r][c]

                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]
                    length = 0

                    while 0 <= nr < n and 0 <= nc < m:
                        # 같은 섬을 만나면 다리 건설 불가
                        if grid[nr][nc] == curr_island:
                            break

                        if grid[nr][nc] == 0:
                            length += 1
                            nr += dr[i]
                            nc += dc[i]

                        elif grid[nr][nc] >= 2 and grid[nr][nc] != curr_island:
                            if length >= 2:  # 섬 간격은 2 이상
                                edges.append((length, curr_island, grid[nr][nc]))
                            break
    return edges


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]

# 섬 마킹 2부터
island_idx = 2
for i in range(n):
    for j in range(m):
        if not visited[i][j] and grid[i][j] == 1:
            island_marking(i, j, island_idx)
            island_idx += 1

# 가능한 다리 목록
edges = bridges()
edges.sort()

# 섬 연결
parent = [i for i in range(island_idx)]
total_cost = 0
connected_edges = 0

for cost, a, b in edges:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        total_cost += cost
        connected_edges += 1


num_islands = island_idx - 2
if connected_edges == num_islands - 1:
    print(total_cost)
else:
    print(-1)