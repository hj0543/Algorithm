TC = int(input())
for tc in range(TC):
    N = int(input())
    prices = list(map(int, input().split()))

    total = 0
    max_price = 0  # 현재 기준 뒤에서 가장 비싼 가격

    # 리스트를 뒤에서부터 순회
    for i in range(N - 1, -1, -1):
        if prices[i] > max_price:
            # 더 비싼 가격을 발견하면 기준점 갱신
            max_price = prices[i]
        else:
            # 기준점보다 낮으면 그 차이만큼 이득 발생
            total += max_price - prices[i]

    print(f'#{tc+1} {total}')