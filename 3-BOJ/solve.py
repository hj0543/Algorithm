import sys
sys.stdin = open('input.txt', 'r')

##################################################
# 14567
import sys
input = sys.stdin.readline
from collections import deque

def topology_sort():
    q = deque()
    result = [1] * (n + 1)

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            indegree[i] -= 1
            result[i] = max(result[i], result[now] + 1)

            if indegree[i] == 0:
                q.append(i)
    print(*result[1:])

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    indegree[e] += 1

topology_sort()