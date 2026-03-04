
n = int(input())

stones = list(map(int, input().split()))

result = 0

for stone in stones:
    result ^= stone

if result != 0:
    print("koosaga")
else:
    print("cubelover")

