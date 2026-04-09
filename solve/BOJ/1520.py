import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def dfs(r, c):
    # 도착하면 
    if r == m - 1 and c == n - 1:
        return 1
    
    if dp[r][c] != -1:
        return dp[r][c]
    
    dp[r][c] = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
            dp[r][c] += dfs(nr, nc)
    
    return dp[r][c]


m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]

# 시작점, 도착점 - 좌상단, 우하단

dp = [[-1] * n for _ in range(m)]
print(dfs(0, 0))
#