import sys
input = sys.stdin.readline

N = int(input().strip())

result1 = N
total = 0

for i in range(1, int(N ** 0.5) + 1): # range안에 들어갈 수 => 약수의 개수의 절반 / 제곱수일 경우 루트
    add = (N // i) - (i - 1)
    total += add

print(total)