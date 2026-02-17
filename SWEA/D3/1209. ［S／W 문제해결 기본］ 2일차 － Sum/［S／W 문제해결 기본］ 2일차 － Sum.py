for tc in range(10):
    N = int(input())
    grid = []
    for _ in range(100):
        grid.append(list(map(int, input().split())))

    total = []
    # 가로
    for i in range(100):
        total.append(sum(grid[i]))

    # 세로
    for i in range(100):
        add = 0
        for j in range(100):
            add += grid[j][i]
        total.append(add)

    # 좌상 - 우하
    add1 = 0
    for i in range(100):
        add1 += grid[i][i]
    total.append(add1)

    # 우상 - 좌하
    add2 = 0
    for i in range(100):
        add2 += grid[i][99-i]
    total.append(add2)

    print(f'#{tc+1} {max(total)}')