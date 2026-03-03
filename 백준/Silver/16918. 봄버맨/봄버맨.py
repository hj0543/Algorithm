import sys
input = sys.stdin.readline

R, C, N = map(int, input().split())
grid = []
for _ in range(R):
    grid.append(list(map(str, input().rstrip())))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 2n
result_A = [['O'] * C for _ in range(R)]

# 4n - 1
result_B = [['O'] * C for _ in range(R)]

for r in range(R):
    for c in range(C):
        if grid[r][c] == 'O':
            result_B[r][c] = '.'
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if 0 <= nr < R and 0 <= nc < C and result_B[nr][nc] == 'O':
                    result_B[nr][nc] = '.'

# 4n + 1
result_C = [['O'] * C for _ in range(R)]

for r in range(R):
    for c in range(C):
        if result_B[r][c] == 'O':
            result_C[r][c] = '.'
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if 0 <= nr < R and 0 <= nc < C:
                    result_C[nr][nc] = '.'

# 결과 출력
if N == 1:
    for i in range(R):
        print(''.join(grid[i]))
elif N % 2 == 0:
    for i in range(R):
        print(''.join(result_A[i]))
elif N >= 3 and (N + 1) % 4 == 0:
    for i in range(R):
        print(''.join(result_B[i]))
elif N >= 5 and (N - 1) % 4 == 0:
    for i in range(R):
        print(''.join(result_C[i]))