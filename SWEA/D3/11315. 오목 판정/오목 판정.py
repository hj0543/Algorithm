TC = int(input())
for tc in range(TC):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(str, input().rstrip())))

    found = False
    # 4방향 (우, 하, 우하 대각선, 좌하 대각선)
    dr = [0, 1, 1, 1]
    dc = [1, 0, 1, -1]

    for r in range(N):
        for c in range(N):
            if board[r][c] == 'o':
                # 'o'를 발견하면 4방향으로 5개가 이어지는지 확인
                for d in range(4):
                    count = 1
                    nr, nc = r + dr[d], c + dc[d]

                    # 해당 방향으로 연속 5개 확인
                    while 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 'o':
                        count += 1
                        if count >= 5:
                            found = True
                            break
                        nr += dr[d]
                        nc += dc[d]
                    if found: break
            if found: break
        if found: break

    if found:
        print(f"#{tc+1} YES")
    else:
        print(f"#{tc+1} NO")