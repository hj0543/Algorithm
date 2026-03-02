import sys
sys.stdin = open('input.txt', 'r')

##################################################
# 1012

import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    M, N, K = map(int,input().split())
    grid = []
    for _ in range(N):
        grid.append([0] * M)
    for _ in range(K):
        x, y = map(int,input().split())
        grid[y][x] = 1

    counts = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:     # 배추 발견
                counts += 1         # 구역 1개 추가
                grid[i][j] = 0      # 방문한 곳은 0으로 처리
                stack = [[i, j]]    #방문한 곳을 담아둘 스택

                while stack:
                    cur_i, cur_j = stack.pop()  # 현재 방문한 곳을 우선 pop, for문 완료 후 전체 pop

                    for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
                        ni, nj = cur_i + di, cur_j + dj

                        if 0 <= ni < N and 0 <= nj < M and grid[ni][nj] == 1:
                            grid[ni][nj] = 0
                            stack.append([ni, nj])

    print(counts)




