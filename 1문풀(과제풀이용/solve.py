import sys
sys.stdin = open('input.txt', 'r')

# 과제풀이용
import sys
input = sys.stdin.readline


# len 함수
def my_len(arr):
    cnt = 0
    for i in arr:
        cnt += 1
    return cnt

# max 함수
def my_max(arr):
    max_v = arr[0]
    for i in range(my_len(arr)):
        if arr[i] > max_v:
            max_v = arr[i]
    return max_v


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    total = [] # 때려잡은 파리 수 list
    for i in range(N - M + 1): # 파리 범위
        for j in range(N - M + 1):

            add = 0 # 한 번 때려잡은 파리 수
            for k in range(i, i + M): # 때려잡을 파리 범위
                for l in range(j, j + M):
                    add += arr[k][l]

            total.append(add) # 때려잡은 파리 무덤에 보내기

    print(f'#{tc} {my_max(total)}')





