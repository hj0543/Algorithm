import sys
input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    d_sq = ((x2 - x1) ** 2)  + ((y2 - y1) ** 2)
    sum_r_sq = (r1 + r2) ** 2
    diff_r_sq = (r1 - r2) ** 2

    # 교점이 무수히 많다 -> 겹친다
    if diff_r_sq == 0 and d_sq == 0:
        print(-1)

    # 교점이 1개다 -> 외점 또는 내접
    elif sum_r_sq == d_sq or diff_r_sq == d_sq:
        print(1)

    # 교점이 2개다 -> 반지름 차의 제곱 < 거리의 제곱 < 반지름 합의 제곱
    elif diff_r_sq < d_sq < sum_r_sq:
        print(2)
    # 교점이 없다 -> 포함 또는 외부
    else:
        print(0)