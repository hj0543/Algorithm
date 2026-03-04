import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

V = 100000
visited = [False] * (V + 1)

q = deque()

# (현재 위치, 현재까지 걸린 시간)
q.append((n, 0))
visited[n] = True

while q:
    x, time = q.popleft()

    # 목표 위치에 도착했다면 그 순간의 시간이 최소 시간
    if x == k:
        print(time)
        break

    for nx in (x - 1, x + 1, x * 2):
        if 0 <= nx <= V and not visited[nx]:
            visited[nx] = True
            q.append((nx, time + 1))