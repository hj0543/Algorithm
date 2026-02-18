TC = int(input())
for tc in range(TC):
    N = int(input())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().rstrip())))

    # N // 2
    total = 0
    # 상위
    for i in range(N // 2):
        total += sum(grid[i][(N // 2) - i:(N // 2 + 1) + i])

    # 중간
    total += sum(grid[N // 2])

    # 하위
    for i in range(N // 2 + 1, N):
        total += sum(grid[i][(N // 2) - (N - 1 - i):(N // 2 + 1) + (N - 1 - i)])

    print(f'#{tc+1} {total}')