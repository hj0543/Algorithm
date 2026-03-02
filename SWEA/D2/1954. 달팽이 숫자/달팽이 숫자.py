TC = int(input())
for tc in range(TC):
    n = int(input())
    grid = [[0] * n for _ in range(n)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    input_dir = 0


    r, c = 0, 0
    num = 1
    grid[r][c] = num
    for i in range((n ** 2) * 2):
        dir = (input_dir + 4) % 4
        nr = r + dr[dir]
        nc = c + dc[dir]

        if 0 <= nr < n and 0 <= nc < n:
            if grid[nr][nc] == 0:
                num += 1
                grid[nr][nc] = num
                r, c = nr, nc
            else:
                input_dir += 1
        else:
            input_dir += 1

    print(f'#{tc+1}')
    for i in range(n):
        print(*grid[i])