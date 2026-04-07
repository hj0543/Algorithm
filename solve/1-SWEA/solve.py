def synergy(mask):
    # mask에 포함된 재료들끼리의 시너지 합을 계산한다.
    flavor = 0
    for i in range(N):
        for j in range(i + 1, N):
            if (mask & (1 << i)) and (mask & (1 << j)):
                flavor += grid[i][j] + grid[j][i]
    return flavor


TC = int(input())

for tc in range(TC):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    min_diff = float('inf')

    # 모든 부분집합 중 재료 개수가 N // 2개인 경우만 선택한다.
    for mask in range(1 << N):
        if bin(mask).count('1') != N // 2:
            continue

        # A 음식에 들어갈 재료 집합
        A = mask
        # B 음식은 전체 집합에서 A를 제외한 나머지 재료 집합
        B = ((1 << N) - 1) ^ mask

        flavor_a = synergy(A)
        flavor_b = synergy(B)

        # 두 음식의 맛 차이 최솟값을 갱신한다.
        min_diff = min(min_diff, abs(flavor_a - flavor_b))

    print(f"#{tc + 1} {min_diff}")
