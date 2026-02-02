import sys
input = sys.stdin.readline

A = [] # 행렬

for _ in range(9):
    A.append(list(map(int, input().split())))

max_number = 0 # 최대값 초기값 설정
x = 0 # 최대값일때 행
y = 0 # 최대값일때 열

for i in range(9):
    for j in range(9):
        if A[i][j] >= max_number: # 최대값 갱신
            max_number = A[i][j]
            x = i + 1
            y = j + 1

print(max_number)
print(x, y)