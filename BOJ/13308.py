# [로직설계]


import sys
input = sys.stdin.readline
import heapq

def dijkstra(start, end):
    min_cost = [[int(1e9)] * (max(prices) + 1) for _ in range(N + 1)]
    
    pq = [(0, start, prices[start - 1])]  # (비용, 도시, 현재 최소 기름값)
    min_cost[start][prices[start - 1]] = 0

    while pq:
        curr_cost, curr_city, curr_min_price = heapq.heappop(pq)

        if curr_city == end:
            return curr_cost

        if curr_cost > min_cost[curr_city][curr_min_price]:
            continue

        for next_city, road_length in graph[curr_city]:
            next_min_price = min(curr_min_price, prices[next_city - 1])
            next_cost = curr_cost + curr_min_price * road_length

            if next_cost < min_cost[next_city][next_min_price]:
                min_cost[next_city][next_min_price] = next_cost
                heapq.heappush(pq, (next_cost, next_city, next_min_price))

    
# --------------------------------------------------------

N, M = map(int, input().split())

prices = list(map(int, input().split()))

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, l = map(int, input().split())
    graph[u].append((v, l))
    graph[v].append((u, l))

result = dijkstra(1, N)
print(result)

