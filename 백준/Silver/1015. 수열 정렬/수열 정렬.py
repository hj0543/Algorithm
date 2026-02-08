import sys


N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

temp = []
for i in range(N):
    temp.append((A[i], i))

temp.sort()

P = [0] * N

for rank in range(N):
    value, idx = temp[rank]
    
    P[idx] = rank

print(*P)