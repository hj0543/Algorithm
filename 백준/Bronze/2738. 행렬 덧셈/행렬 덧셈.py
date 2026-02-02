import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A = [] # 첫 번째 행렬
B = [] # 두 번째 행렬

# 각각 나누어 담기
for _ in range(1):
    for i in range(N):
        A.append(list(map(int, input().split())))
    for i in range(N):
        B.append(list(map(int, input().split())))

# 두 행렬의 덧셈을 담을 행렬
result = []

for i in range(N):
    for j in range(M):
        add = A[i][j] + B[i][j]
        result.append(add)

# result -> 4 4 4 6 6 6 5 6 100

for i in range(0, len(result), M):
    print(*result[i:i+M])