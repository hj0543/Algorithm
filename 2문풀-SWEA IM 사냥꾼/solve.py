import sys
sys.stdin = open('input.txt', 'r')

##################################################

TC = int(input())
for tc in range(TC):
    N = int(input())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))

    # 8방향 정의 (상, 하, 좌, 우, 좌상, 우상, 좌하, 우하)
    dr = [-1, 1, 0, 0, -1, -1, 1, 1]
    dc = [0, 0, -1, 1, -1, 1, -1, 1]

    total = 0  # 잡은 토끼의 총합

    # 1. 지도 전체 탐색
    for r in range(N):
        for c in range(N):
            # 2. 사냥꾼(1)을 찾았을 때만 8방향 발사
            if grid[r][c] == 1:
                for i in range(8):
                    nr, nc = r + dr[i], c + dc[i]





