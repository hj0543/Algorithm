def backtracking(r, c, current_sum):
    global min_sum
 
    # 가지치기
    if current_sum >= min_sum:
        return
 
    if r == n - 1 and c == n - 1:
        min_sum = min(min_sum, current_sum)
        return
 
    for dr, dc in [(0, 1), (1, 0)]:
        nr, nc = r + dr, c + dc
 
        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
            visited[nr][nc] = True
            backtracking(nr, nc, current_sum + grid[nr][nc])
            visited[nr][nc] = False  # 복구
 
 
TC = int(input())
for tc in range(TC):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
 
    visited = [[False] * n for _ in range(n)]
    min_sum = float('inf')
 
    visited[0][0] = True
    backtracking(0, 0, grid[0][0])
 
    print(f"#{tc+1} {min_sum}")