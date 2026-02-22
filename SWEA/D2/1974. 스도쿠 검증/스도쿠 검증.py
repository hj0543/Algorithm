TC = int(input())
for tc in range(TC):
    grid = []
    for _ in range(9):
        grid.append(list(map(int, input().split())))

    # 3*3 격자내부 검사
    flag = True
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            stack = []
            for k in range(3):
                for l in range(3):
                    if grid[i+k][j+l] not in stack:
                        stack.append(grid[i+k][j+l])
                    else:
                        flag = False
                        break
                if not flag: break
            if not flag: break
        if not flag: break
    if not flag:
        print(f'#{tc+1} 0')
        continue

    # 세로 검사
    for i in range(9):
        stack = []
        for j in range(9):
            if grid[j][i] not in stack:
                stack.append(grid[j][i])
            else:
                flag = False
                break
        if not flag: break
    if not flag:
        print(f'#{tc+1} 0')
        continue

    # 가로 검사
    for i in range(9):
        stack = []
        for j in range(9):
            if grid[i][j] not in stack:
                stack.append(grid[i][j])
            else:
                flag = False
                break
        if not flag: break
    if not flag:
        print(f'#{tc+1} 0')
        continue
    else:
        print(f'#{tc+1} 1')