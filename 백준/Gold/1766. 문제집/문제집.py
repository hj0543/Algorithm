# BOJ 1766 - 문제집
import sys
input = sys.stdin.readline
import heapq

def topology_sort():
    result = []
    q = []

    for i in range(1, n + 1):
        if indegree[i] == 0:
            heapq.heappush(q, i)

    while q:
        now = heapq.heappop(q)
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(q, i)

    return result


# ----------------------------------------

# 입력부

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

print(*topology_sort())