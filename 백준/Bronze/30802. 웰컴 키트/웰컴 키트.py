N = int(input())
S = list(map(int, input().split()))
T, P = list(map(int, input().split()))

total = 0
for i in range(len(S)):
    if S[i] % T == 0:
        total += (S[i] / T)
    elif S[i] % T != 0:
        total += (S[i] // T + 1)

a = N // P
b = N % P

print(int(total))
print(a, b)