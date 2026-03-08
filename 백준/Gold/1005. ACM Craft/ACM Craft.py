import sys
input = sys.stdin.readline
from collections import deque

def topology_sort():
    q = deque()

    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if indegree[i] == 0:
            dp[i] = time[i]

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            dp[i] = max(dp[i], dp[now] + time[i])
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    print(dp[w])

TC = int(input())
for tc in range(TC):
    n, k = map(int, input().split())

    time_data = list(map(int, input().split()))
    time = [0] * (n + 1)
    for i in range(1, len(time_data)+1):
        time[i] = time_data[i-1]

    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for i in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1

    w = int(input())

    topology_sort()