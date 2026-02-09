import sys
input = sys.stdin.readline

N, M = map(int,input().split())

listen = []
see = []

for n in range(N):
    listen.append(input().rstrip())
for m in range(M):
    see.append(input().rstrip())

L = set(listen)
S = set(see)

result = sorted(list(L & S))
print(len(result))
for r in result:
    print(r)
    