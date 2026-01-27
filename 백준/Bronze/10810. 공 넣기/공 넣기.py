N, M = map(int, input().split())

baskets = [0] * N  # 바구니 상태 초기화

for x in range(M):
    i, j, k = map(int, input().split())
    baskets[i-1:j] = [k] * (j - i + 1) # i부터 j까지 k로 바꾼다.

print(*baskets)