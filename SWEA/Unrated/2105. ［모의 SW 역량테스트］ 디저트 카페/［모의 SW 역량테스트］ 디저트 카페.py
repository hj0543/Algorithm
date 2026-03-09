dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]
 
 
def dfs(r, c, d, count):
    global max_desserts, sr, sc
 
    if d == 3 and r == sr and c == sc:  # d == 3 없으면 그대로 종료 됨...
        max_desserts = max(max_desserts, count)
        return
 
    # 방향전환로직
    for i in range(d, d + 2):
        if i < 4:
            nr, nc = r + dr[i], c + dc[i]
 
            if 0 <= nr < n and 0 <= nc < n:
                # 출발점으로 돌아온 경우
                if nr == sr and nc == sc:
                    dfs(nr, nc, i, count)
 
                # 처음 먹어보는 디저트인 경우
                elif not visited[grid[nr][nc]]:
                    visited[grid[nr][nc]] = True
                    dfs(nr, nc, i, count + 1)
                    visited[grid[nr][nc]] = False
 
 
TC = int(input())
for tc in range(TC):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
 
    max_desserts = -1
    visited = [False] * 101
 
    # 시작점 설정
    for r in range(n - 2):
        for c in range(1, n - 1):
            sr, sc = r, c
            visited[grid[r][c]] = True
            dfs(r, c, 0, 1)  # (현재 r, 현재 c, 현재 방향, 먹은 개수)
            visited[grid[r][c]] = False
 
    print(f"#{tc+1} {max_desserts}")