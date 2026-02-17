TC = int(input())

for tc in range(TC):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    result = []
    for i in range(N):
        rotate1 = ''
        for j in range(N):
            rotate1 += str(board[N-j-1][i])
        result.append(rotate1)

        rotate2 = ''
        for j in range(N):
            rotate2 += str(board[N-i-1][N-j-1])
        result.append(rotate2)

        rotate3 = ''
        for j in range(N):
            rotate3 += str(board[j][N-i-1])
        result.append(rotate3)

    print(f'#{tc+1}')
    for i in range(N):
        print(*result[i*3:i*3+3])