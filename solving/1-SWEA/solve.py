import sys
sys.stdin = open('input.txt', 'r')

##################################################
# 문제풀이 2 - 장훈이의 높은 선반

# [로직설계]
# 1. N 명의 점원을 다양하게 선택
# 1-1. R명 선택 기준이 없다 -> 부분집합 문제, 집합에 포함 된다 or 안된다

# 2. 가지치기
# 2-1. 이미 높이가 b이상이다.

# depth : N명의 점원을 검토 (N)
# branch : 집합에 현재 원소가 포함 O, X (두 가지)
def recur(idx, total_height):
    global min_answer

    # 가지치기
    if total_height >= B:
        min_answer = min(min_answer, total_height)
        return

    # 종료조건    
    if idx == N:
        return

    # idx 번째 점원이 집합에 포함 되는 경우
    recur(idx + 1, total_height + heights[idx])

    # idx 번째 점원이 집합에 포함 안되는 경우
    recur(idx + 1, total_height)


T = int(input())

for tc in range(1, TC + 1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    min_answer = float(inf) # 10000 * N
    recur(0, 0)
    print(f'#{tc} {min_answer - B}')
















