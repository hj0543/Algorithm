import sys
sys.stdin = open('input.txt', 'r')

##################################################

TC = int(input())

for tc in range(TC):
    N, M = map(int,input().split())

    dr = [-1, 0, 1, 0, -1, 1, 1, -1]
    dc = [0, 1, 0, -1, 1, 1, -1, -1]

    grid = [[0] * (N+1) for _ in range(N+1)]
    grid[N//2][N//2] = 2
    grid[N//2+1][N//2+1] = 2
    grid[N//2+1][N//2] = 1
    grid[N//2][N//2+1] = 1

    for i in range(M):
        c, r, s = map(int,input().split())

        for j in range(M):
            grid[r][c] = s

            for k in range(8):
                nr = r + dr[k]
                nc = c + dc[k]

                flip = []
                while 1 <= nr <= N and 1 <= nc <= N and grid[nr][nc] == 3 - grid[r][c]:
                    flip.append((nr, nc))
                    nr += dr[k]
                    nc += dc[k]

                    if 1 <= nr <= N and 1 <= nc <= N and grid[nr][nc] == grid[r][c]:
                        for fr, fc in flip:
                            grid[fr][fc] = grid[r][c]

    result1 = 0
    result2 = 0

    for i in range(1, N+1):
        for j in range(1, N+1):
            if grid[i][j] == 1:
                result1 += 1
            elif grid[i][j] == 2:
                result2 += 1

    print(f'#{tc+1} {result1} {result2}')