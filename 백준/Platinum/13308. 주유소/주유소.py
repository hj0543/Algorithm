import sys
input = sys.stdin.readline
import heapq

def dijkstra(start, end):
    
    # 각 도시까지의 최소 비용 저장
    min_cost = [float('inf')] * (N + 1)
    min_cost[start] = 0

    pq = [(0, start)] # (비용, 도시 번호)
    while pq:
        curr_cost, curr_city = heapq.heappop(pq)

        if curr_city == end:
            return curr_cost

        if curr_cost > min_cost[curr_city]:
            continue

        for next_city, road_length in graph[curr_city]:
            next_cost = curr_cost + prices[curr_city - 1] * road_length

            if next_cost < min_cost[next_city]:
                min_cost[next_city] = next_cost
                heapq.heappush(pq, (next_cost, next_city))

    
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