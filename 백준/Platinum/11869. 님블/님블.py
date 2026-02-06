import sys
input = sys.stdin.readline

M = int(input().strip())
positions = list(map(int, input().split()))

xor_sum = 0
for p in positions:
    xor_sum ^= p

if xor_sum != 0:
    print("koosaga")
else:
    print("cubelover")