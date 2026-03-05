import sys
sys.stdin = open('input.txt', 'r')

##################################################
# 1325
import sys
input = sys.stdin.readline
from collections import deque

def bfs(s):
    visited = [False] * (n + 1)

    queue = deque([s])

    visited[s] = True
    count = 1

    while queue:
        v = queue.popleft()

        for w in graph[v]:
            if not visited[w]:
                visited[w] = True
                queue.append(w)
                count += 1
    return count

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e = map(int, input().split())

    graph[e].append(s)

max_counts = 0
result = []

for i in range(1, n + 1):
    cnt = bfs(i)

    if cnt > max_counts:
        max_counts = cnt
        result = [i]
    elif cnt == max_counts:
        result.append(i)

print(*result)