def dfs(curr, count, total):
    global min_cons
 
    # 가지치기
    if total >= min_cons:
        return
 
    if count == n:
        total += grid[curr][0]
        min_cons = min(min_cons, total)
        return
 
    for next_room in range(1, n):
        if not visited[next_room]:
            visited[next_room] = True
            dfs(next_room, count + 1, total + grid[curr][next_room])
            visited[next_room] = False  # 복구
 
 
TC = int(input())
for tc in range(TC):
    n = int(input())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    visited = [False] * n
    visited[0] = True
 
    min_cons = float('inf')
    dfs(0, 1, 0)
    print(f'#{tc + 1} {min_cons}')