import sys
sys.stdin = open('input.txt', 'r')

# 과제풀이용
import sys
input = sys.stdin.readline

TC = int(input())

for tc in range(TC):
    N, M = map(int, input().split())

    board = []

    for i in range(N):
        board.append(list(input().rstrip()))

    row_words = []
    column_words = []

    # row_words 에 M의 길이만큼 잘라서 넣기
    for i in range(N):
        for j in range(N - M + 1):
            temp1 = []
            for k in range(M):
                temp1.append(board[i][j+k])
            row_words.append(temp1)

    # column_words 에 M의 길이만큼 잘라서 넣기
    for i in range(N):
        for j in range(N - M + 1):
            temp2 = []
            for k in range(M):
                temp2.append(board[j+k][i])
            column_words.append(temp2)

    result = ''

    for i in range(len(row_words)):
        if row_words[i] == row_words[i][::-1]:
            result = row_words[i]

    for i in range(len(column_words)):
        if column_words[i] == column_words[i][::-1]:
            result = column_words[i]

    print(f'#{tc+1} {"".join(result)}')


