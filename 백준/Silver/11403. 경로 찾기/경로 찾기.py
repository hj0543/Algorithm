def dfs(s, v, d):
    visited[v] = True
    dist[v] = d

    for w in graph[v]:
        if w == s:  # 시작점으로 돌아오는 간선을 발견하면
            cycle[s] = True  # 사이클 존재 표시
        if not visited[w]:
            dfs(s, w, d + 1)

n = int(input())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

graph = [[] for _ in range(n + 1)]


for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            graph[i].append(j)

result = [[0] * n for _ in range(n)]

for i in range(n):
    visited = [False] * (n + 1)
    dist = [0] * (n + 1)
    cycle = [False] * (n + 1)

    dfs(i, i, 0)

    for j in range(n):
        if i != j and visited[j]:
            result[i][j] = 1
        if i == j and cycle[i]:
            result[i][i] = 1

for i in range(n):
    print(*result[i])