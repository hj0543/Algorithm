import heapq

INF = 10**9


def dijkstra(start, n, adj):
    distance = [INF] * (n + 1)
    pq = [(0, start)]
    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        if distance[now] < dist:
            continue

        for nxt, weight in adj[now]:
            cost = dist + weight
            if cost < distance[nxt]:
                distance[nxt] = cost
                heapq.heappush(pq, (cost, nxt))

    return distance


T = int(input())

for tc in range(1, T + 1):
    n, e = map(int, input().split())
    adj = [[] for _ in range(n + 1)]

    for _ in range(e):
        s, e, w = map(int, input().split())
        adj[s].append((e, w))

    distance = dijkstra(0, n, adj)
    print(f"#{tc} {distance[n]}")