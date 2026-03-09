import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

V, E, N = map(int, input().split())

graph = [[] for _ in range(V + 1)]

for i in range(E):
    s, e = map(int, input().split())

    graph[s].append(e)
    graph[e].append(s)

for i in range(1, V + 1):
    graph[i].sort()

def dfs(v):
    visited_dfs[v] = True
    print(v, end=' ')

    for w in graph[v]:
        if not visited_dfs[w]:
            dfs(w)

def bfs(start_v):
    q = deque([start_v])
    visited_bfs[start_v] = True

    while q:
        v = q.popleft()
        print(v, end=' ')

        for w in graph[v]:
            if not visited_bfs[w]:
                visited_bfs[w] = True
                q.append(w)


visited_dfs = [False] * (V + 1)
dfs(N)
print()

visited_bfs = [False] * (V + 1)
bfs(N)
print()