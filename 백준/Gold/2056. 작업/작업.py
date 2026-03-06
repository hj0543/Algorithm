import sys
input = sys.stdin.readline
from collections import deque

def topology_sort():
    q = deque()
    # result = []

    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if indegree[i] == 0:
            dp[i] = time[i]

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        # result.append(now)

        for i in graph[now]:
            dp[i] = max(dp[i], dp[now] + time[i])
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    print(max(dp))

n = int(input())

time = [0] * (n + 1)
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]

    if data[1] > 0:
        for pre in data[2:]:
            graph[pre].append(i)  # 선행 작업이 끝나야 현재 작업(i)을 할 수 있음
            indegree[i] += 1

topology_sort()