import sys
sys.stdin = open('input.txt', 'r')

##################################################
# 문제풀이 1 - 벽돌깨기

# [로직전략]
# 1. 남은 벽돌 세는 함수
# 1-1. 2중 for문 완탐

# 2. 중력 함수
# 2-1. 0이 아닌 숫자만 stack에 쌓고
# 2-2. 배열 아래에서부터 다시 채우기

# 3. 연쇄폭발 함수(BFS)
# 3-1. 모든 연쇄폭발 시행하고 벽돌 떨어뜨리기
# 3-2. bfs로 벽돌에 적힌 숫자만큼 폭발, 연쇄작용

# 4. 구슬 위치 찾기(백트래킹)
# 4-1. 종료조건 : 남은 벽돌이 없거나 구슬을 모두 썼거나
# 4-2. 열의 가장 위에 위치한 벽돌의 인덱스값 찾기
# 4-3-1. 벽돌 없으면 다음 벽돌 넘기기

from collections import deque

# 1. 현재 남아있는 벽돌 세기
def count_bricks(arr):
    counts = 0
    for row in arr:
        for cell in row:
            if cell > 0:
                counts += 1
    return counts

# 2. 벽돌 폭발 후 위에 있는 벽돌 떨어뜨리는 함수
def gravity(arr):
    for x in range(W):
        # 0이 아닌 숫자만 stack에 쌓고 배열 아래에서부터 다시 채우기
        stack = []
        for y in range(H):
            if arr[y][x] > 0:
                stack.append(arr[y][x])
                arr[y][x] = 0

        # 아래 칸부터 다시 채우기
        idx = H - 1
        while stack:
            arr[idx][x] = stack.pop()
            idx -= 1

# 3. 연쇄폭발 함수
def burst(sy, sx, arr):
    q = deque([(sy, sx, arr[sy][sx])])
    arr[sy][sx] = 0

    while q:
        y, x, power = q.popleft()   # power : 해당 벽돌에 적힌 수
        if power <= 1:
            continue

        # 벽돌에 적힌 숫자 - 1 만큼 4방향으로 확산
        for p in range(1, power):
            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ny = y + dy * p
                nx = x + dx * p

                if 0 <= ny < H and 0 <= nx < W and arr[ny][nx] > 0:
                    q.append((ny, nx, arr[ny][nx]))
                    arr[ny][nx] = 0


# 4. 구슬 떨어뜨리는 모든 경우의 수
def drop_marble(counts, current_map):
    global min_bricks

    # 현재 남아있는 벽돌 계산
    remain = count_bricks(current_map)

    # 종료조건 1 : 구슬을 모두 소진한 경우
    if N == counts:
        min_bricks = min(min_bricks, remain)
        return

    # 종료조건 2 : 남아있는 벽돌이 없는 경우
    if remain == 0:
        min_bricks = 0
        return

    # 열의 가장 위에 위치한 벽돌 찾기
    for x in range(W):
        temp_map = [row[:] for row in current_map]
        target_y = -1
        for y in range(H):
            if temp_map[y][x] > 0:
                target_y = y
                break

        # 벽돌이 존재하는 경우
        if target_y != -1:
            burst(target_y, x, temp_map)
            gravity(temp_map)
            drop_marble(counts + 1, temp_map)

        # 벽돌이 존재하지 않는 경우
        else:
            drop_marble(counts + 1, temp_map)

TC = int(input())

for tc in range(TC):
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]

    min_bricks = float('inf')
    drop_marble(0, board)

    print(f"#{tc+1} {min_bricks}")


