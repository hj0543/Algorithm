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

        for nxt, cost in adj[now]:
            next_dist = dist + cost
            if next_dist < distance[nxt]:
                distance[nxt] = next_dist
                heapq.heappush(pq, (next_dist, nxt))

    return distance


T = int(input())

for tc in range(1, T + 1):
    # n: 마을에 있는 총 집의 개수 / x: 인수의 집
    n, m, x = map(int, input().split())

    # 왕복이기 때문에 역방향도 만듦.
    graph = [[] for _ in range(n + 1)]
    reverse_graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        # start에서 end까지 가중치가 cost
        start, end, cost = map(int, input().split())
        graph[start].append((end, cost))
        reverse_graph[end].append((start, cost))

    # x번 집으로 가는거
    go = dijkstra(x, n, graph)
    
    # 생파하고 다시 돌아오는거
    back = dijkstra(x, n, reverse_graph)

    result = 0
    for node in range(1, n + 1):
        result = max(result, go[node] + back[node])

    print(f"#{tc} {result}")