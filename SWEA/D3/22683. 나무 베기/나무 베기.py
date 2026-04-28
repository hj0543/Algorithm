from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def bfs(sr, sc):
    queue = deque()
    # r, c, 남은 벌목 횟수, 방향(상우하좌), 조작 횟수
    queue.append((sr, sc, k, 0, 0))  
    visited[sr][sc][k][0] = True

    while queue:
        r, c, cut, d, cnt = queue.popleft()

        # 도착 지점에 도달하면 cnt출력
        if field[r][c] == 'Y':
            return cnt
        
        # 1. 전진
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < n and 0 <= nc < n:

            # 가고자 하는 길에 나무가 있을 때
            if field[nr][nc] == 'T':
                if cut > 0 and not visited[nr][nc][cut - 1][d]:
                    visited[nr][nc][cut - 1][d] = True
                    queue.append((nr, nc, cut - 1, d, cnt + 1))
            
            # 가고자 하는 길에 나무가 없을 때 ('G')
            else:
                if not visited[nr][nc][cut][d]:
                    visited[nr][nc][cut][d] = True
                    queue.append((nr, nc, cut, d, cnt + 1))
                
        # 2. 오른쪽 90회전
        nd = (d + 1) % 4
        if not visited[r][c][cut][nd]:
            visited[r][c][cut][nd] = True
            queue.append((r, c, cut, nd, cnt + 1))


        # 3. 왼쪽 회전
        nd = (d - 1) % 4
        if not visited[r][c][cut][nd]:
            visited[r][c][cut][nd] = True
            queue.append((r, c, cut, nd, cnt + 1))

    return -1


T = int(input())
for tc in range(1, T + 1):
    n, k = map(int, input().split())
    field = [list(input()) for _ in range(n)]

    # 출발 지점 정보
    sr, sc = 0, 0
    for i in range(n):
        for j in range(n):
            if field[i][j] == 'X':
                sr, sc = i, j

    # visited 4차원 배열 생성
    visited = [[[[False] * 4 for _ in range(n)] for _ in range(n)] for _ in range(n)]

    print(f'#{tc} {bfs(sr, sc)}')