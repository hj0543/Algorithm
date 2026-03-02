import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

def dfs(curr):
    global count
    visited[curr] = count
    
    for next_node in graph[curr]:
        if visited[next_node] == 0:
            count += 1
            dfs(next_node)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
count = 1

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(1, n + 1):
    graph[i].sort()

dfs(r)

print('\n'.join(map(str, visited[1:])))