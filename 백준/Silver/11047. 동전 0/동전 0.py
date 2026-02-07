import sys
input = sys.stdin.readline

N, K = map(int,input().split()) # 10 4200
temp = []  # ['1', '5', '10', '50', '100', '500', '1000', '5000', '10000', '50000']

for _ in range(N):
    c = input().rstrip()
    temp.append(c)

coins = temp[::-1]  # ['50000', '10000', '5000', '1000', '500', '100', '50', '10', '5', '1']

remain_coins = K
counts = 0

i = 0
# print(coins[i])
while remain_coins > 0:
    if remain_coins // int(coins[i]) >= 1:
        counts += remain_coins // int(coins[i])
        remain_coins -= int(coins[i]) * (remain_coins // int(coins[i]))
    else:
        i += 1

print(counts)