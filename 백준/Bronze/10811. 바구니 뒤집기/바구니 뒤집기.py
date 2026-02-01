N, M = map(int, input().split())

basket = list(range(1, N + 1))


for _ in range(M):
    i, j = map(int, input().split())

    basket[i-1 : j] = basket[i-1 : j][::-1] # 범위 list 뽑아와서 역변화 후 다시 삽입


print(*basket)