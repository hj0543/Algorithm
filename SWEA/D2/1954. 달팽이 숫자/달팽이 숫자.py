TC = int(input())

for tc in range(TC):
    N = int(input())
    grid = [[0] * N for _ in range(N)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    r, c = 0, 0

    dir_num = [0, 1, 2, 3]
    input_dir = 0


    grid[r][c] = 1
    number = 2
    for i in range(N ** 2 * 2):
        cur_dir = (input_dir + 4) % 4
        nr = r + dr[cur_dir]
        nc = c + dc[cur_dir]
        if 0 <= nr < N and 0 <= nc < N:
            if grid[nr][nc] == 0:
                grid[nr][nc] = number
                r, c = nr, nc
                number += 1
            else:
                input_dir += 1
        else:
            input_dir += 1

    print(f'#{tc+1}')
    for j in range(N):
        print(*grid[j])