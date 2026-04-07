import heapq
 
INF = 10**9
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
 
 
def dijkstra(grid, n):
    dist = [[INF] * n for _ in range(n)]
    pq = [(0, 0, 0)]
    dist[0][0] = 0
 
    while pq:
        cost, r, c = heapq.heappop(pq)
 
        if dist[r][c] < cost:
            continue
 
        if r == n - 1 and c == n - 1:
            return cost
 
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
 
            if not (0 <= nr < n and 0 <= nc < n):
                continue
 
            next_cost = cost + 1
            if grid[nr][nc] > grid[r][c]:
                next_cost += grid[nr][nc] - grid[r][c]
 
            if next_cost < dist[nr][nc]:
                dist[nr][nc] = next_cost
                heapq.heappush(pq, (next_cost, nr, nc))
 
    return dist[n - 1][n - 1]
 
# ------------------------------------------------------------
 
T = int(input())
 
for tc in range(1, T + 1):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
 
    result = dijkstra(grid, n)
    print(f"#{tc} {result}")