import sys
sys.stdin = open('input.txt', 'r')

##################################################

# [로직전략]
# 1. 2개를 뽑는 모든 경우의 수를 구해서 시너지 계산하기 (itertools 사용해도 됨?)
# 2. A, B 따로 담아두기
# 3. 완탐으로 순회하면서 최소값 갱신
from itertools import combinations

def synergy(ingredients, grid):
    flavor = 0
    # 그룹 내에서 2개를 뽑는 모든 조합
    for i, j in combinations(ingredients, 2):
        flavor += grid[i][j] + grid[j][i]
    return flavor


TC = int(input())

for tc in range(TC):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # 0부터 N-1
    all_ingredients = list(range(N))
    min_diff = float('inf')

    # N개 중 N/2개를 뽑는 모든 조합 순회
    for A in combinations(all_ingredients, N // 2):

        B = []  # 나머지가 B
        for x in all_ingredients:
            if x not in A:
                B.append(x)

        # 각 음식의 맛 계산
        flavor_a = synergy(A, grid)
        flavor_b = synergy(B, grid)

        # 차이의 최솟값 갱신
        diff = abs(flavor_a - flavor_b)
        min_diff = min(diff, min_diff)

    print(f"#{tc + 1} {min_diff}")








