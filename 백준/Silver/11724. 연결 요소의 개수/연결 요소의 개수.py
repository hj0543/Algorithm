import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(v):
    visited[v] = True

    for w in graph[v]:
        if not visited[w]:
            dfs(w)

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited = [False] * (n + 1)
counts = 0

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        counts += 1

print(counts)