N, M = map(int, input().split())
cards = list(map(int, input().split()))

cards_sum = []       # 3장의 합과 가깝게 만들어야하는 숫자의 차이

for i in range(N):
    for j in range(N):
        for k in range(N):
            if i != j and j != k and k != i:                    # 3장이 각각 다르고
                if cards[i] + cards[j] + cards[k] <= M:          # 3장의 합이 M을 넘지 않을 때
                    add = cards[i] + cards[j] + cards[k]        # 3장의 합을 add 변수 선언
                    cards_sum.append(add)                            # diff 리스트에 담아두기

print(max(cards_sum)) # 최댓값 출력