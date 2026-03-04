import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

def bfs(start, goal, graph):
    queue = deque([start])
    visited[start] = 0

    while queue:
        v = queue.popleft()

        if v == goal:
            return visited[goal]

        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[v] + 1

    return -1

print(bfs(a, b, graph))