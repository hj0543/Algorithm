TC = int(input())
for tc in range(TC):
    N, K = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))

    total = 0

    # 가로 검사
    for i in range(N):
        counts = 0
        for j in range(N):
            if grid[i][j] == 1:
                counts += 1
            else:
                if counts == K:
                    total += 1
                counts = 0
        if counts == K:
            total += 1


    # 세로 검사
    for i in range(N):
        counts = 0
        for j in range(N):
            if grid[j][i] == 1:
                counts += 1
            else:
                if counts == K:
                    total += 1
                counts = 0
        if counts == K:
            total += 1

    print(f'#{tc+1} {total}')