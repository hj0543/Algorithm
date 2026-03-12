# 문제풀이 1 - 탈주범 검거

# [로직전략]
# 1. 4방향 델타를 기반으로 7개의 터널 구조물 리스트 만들기
# 2. 연결확인 로직(bfs)
# 2-1. 본인의 위치가 이미 1시간임
# 2-2. 가지치기 : 현재 위치까지 오는 시간이 이미 L이면 이동불가
# 2-3. 반대방향 로직 체크

from collections import deque

# 1. 터널 구조물 리스트 만들기
# 상 우 하 좌 (시계방향)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 각 파이프 번호가 갈 수 있는 방향
pipe = [
    [],              # 0 (없음)
    [0, 1, 2, 3],    # 1
    [0, 2],          # 2
    [1, 3],          # 3
    [0, 1],          # 4
    [1, 2],          # 5
    [2, 3],          # 6
    [0, 3]           # 7
]

# 반대 방향 체크 (상<->하, 좌<->우)
opp = {0: 2, 2: 0, 1: 3, 3: 1}


# 2. 연결확인 로직
def bfs(sr, sc, L):
    q = deque([(sr, sc)])
    visited[sr][sc] = 1

    counts = 1

    while q:
        r, c = q.popleft()

        # 2-2. 현재 위치까지 오는데 걸린 시간이 L이면 더 이상 이동 불가
        if visited[r][c] >= L:
            continue

        for d in pipe[board[r][c]]:
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < M:
                if visited[nr][nc] == 0 and board[nr][nc] > 0:

                    # 2-3. 연결 확인 로직(반대 방향)
                    if opp[d] in pipe[board[nr][nc]]:
                        visited[nr][nc] = visited[r][c] + 1
                        q.append((nr, nc))
                        counts += 1

    return counts



TC = int(input())
for tc in range(TC):
    N, M, R, C, L = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0] * M for _ in range(N)]

    result = bfs(R, C, L)

    print(f'#{tc+1} {result}')