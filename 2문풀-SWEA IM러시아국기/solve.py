import sys
sys.stdin = open('input.txt', 'r')

##################################################

TC = int(input())
for tc in range(TC):
    N, M = map(int, input().split())
    flag = []
    for i in range(N):
        flag.append(list(map(str, input().rstrip())))

    cost = [[0] * 3 for _ in range(N)] # 각 줄에 색 바꾸는 거 저장

    for r in range(N):
        w_cnt = flag[r].count('W')
        b_cnt = flag[r].count('B')
        r_cnt = flag[r].count('R')

        cost[r][0] = M - w_cnt  # W로 만들 때 바꿔야 하는 개수
        cost[r][1] = M - b_cnt  # B로 만들 때 바꿔야 하는 개수
        cost[r][2] = M - r_cnt  # R로 만들 때 바꿔야 하는 개수

    min_cost = float('inf')     # 최소값 초기설정

    for i in range(0, N - 2):               # 위, 아래 흰색, 빨간색은 제외
        for j in range(i + 1, N - 1):
            current_sum = 0                 # 총 비용 초기값 설정

            for r in range(0, i + 1):       # 흰색 구간
                current_sum += cost[r][0]

            for r in range(i + 1, j + 1):   # 파란색 구간
                current_sum += cost[r][1]

            for r in range(j + 1, N):       # 빨간색 구간
                current_sum += cost[r][2]

            if current_sum < min_cost:      # 최소비용 갱신
                min_cost = current_sum

    print(f'#{tc+1} {min_cost}')