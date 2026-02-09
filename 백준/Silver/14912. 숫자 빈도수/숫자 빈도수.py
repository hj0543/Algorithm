N, d = map(str, input().split())
N = int(N)

cnt = 0
for i in range(1, N + 1):
    cnt += str(i).count(d)

print(cnt)