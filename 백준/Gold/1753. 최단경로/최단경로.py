# [로직 설계]


import sys
input = sys.stdin.readline
import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            next_node = i[0]
            weight = i[1]
            cost = dist + weight

            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))

# --------------------------------------------------------

V, E = map(int, input().split())
K = int(input())

min_dist = int(1e9)

graph = [[] for _ in range(V + 1)]
distance = [min_dist] * (V + 1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dijkstra(K)

for i in range(1, V + 1):
    if distance[i] == min_dist:
        print('INF')
    else:
        print(distance[i])