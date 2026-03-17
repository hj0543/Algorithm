# [로직설계]
# 1. 

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

# 보석정보 -> 무게, 가격
jewel = []
for _ in range(N):
    jewel.append(tuple(map(int, input().split())))

# 가방
bag = []
for _ in range(K):
    bag.append(int(input()))

# print(jewel)
# print(bag)




    # 내림차순 정렬
    W.sort(reverse=True)
    T.sort(reverse=True)
 
    total_weight = 0
    w_idx = 0  # 컨테이너
    t_idx = 0  # 트럭
 
    while w_idx < n and t_idx < m:
        if T[t_idx] >= W[w_idx]:
            total_weight += W[w_idx]
            t_idx += 1  # 다음 트럭
            w_idx += 1  # 다음 컨테이너
        else:
            w_idx += 1
 
    print(f'#{tc+1} {total_weight}')