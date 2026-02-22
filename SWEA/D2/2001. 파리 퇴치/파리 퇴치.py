TC = int(input())

for tc in range(TC):
    N, M = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))

    total = []
    for i in range(N - M + 1):      # +1 잊지말것
        for j in range(N - M + 1):
            hit = 0
            for k in range(M):
                for l in range(M):
                    hit += grid[i+k][j+l]
            total.append(hit)

    print(f'#{tc+1} {max(total)}')