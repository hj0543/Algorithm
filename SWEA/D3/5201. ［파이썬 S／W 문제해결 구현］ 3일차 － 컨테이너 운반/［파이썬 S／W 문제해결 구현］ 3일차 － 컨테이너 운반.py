
TC = int(input())

for tc in range(TC):
    N, M = map(int, input().split())
    
    weights = list(map(int, input().split()))
    capacities = list(map(int, input().split()))

	# sort(reverse=True) -> 내림차순
    weights.sort(reverse=True)
    capacities.sort(reverse=True)

    total_weight = 0
    w_idx = 0  # 컨테이너
    t_idx = 0  # 트럭

    while w_idx < N and t_idx < M:
        # 현재 트럭이 현재 컨테이너를 감당할 수 있다면
        if capacities[t_idx] >= weights[w_idx]:
            total_weight += weights[w_idx]
            t_idx += 1  # 다음 트럭
            w_idx += 1  # 다음 컨테이너
        else:
            # 컨테이너가 너무 무거우면 다음 컨테이너 확인
            w_idx += 1

    print(f"#{tc+1} {total_weight}")