import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))

temp = []
result = [0] * N

for i, v in enumerate(X): # 튜플로 묶어서 원래 위치 기억
    temp.append((v, i))

temp.sort(key=lambda x: x[0]) # 좌표를 기준으로 오름차순 정렬

# print(temp)  [(-10, 2), (-9, 4), (2, 0), (4, 1), (4, 3)]
# print(len(temp)) # 5

result[temp[0][1]] = 0      # 첫 번째는 무조건 가장 작다
cnt = 0                     # 초기값 설정

for i in range(1, N):
    if temp[i][0] != temp[i-1][0]:  # 이전 수와 같지 않다면
        cnt += 1                    # 카운트 1증가
    result[temp[i][1]] = cnt        # cnt가 곧 나보다 작은 수의 개수다.

print(*result)
