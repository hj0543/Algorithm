import sys
input = sys.stdin.readline

N = int(input())
data = []
for i in range(N):
    data.append(list(map(int, input().split())))
T = []
P = []
for i in range(N):
    T.append(data[i][0])
    P.append(data[i][1])

dp = [0] * (N+1)
for i in range(N-1, -1, -1):
    time = i + T[i]
    if time <= N:
        dp[i] = max(P[i] + dp[time], dp[i+1])
    else:
        dp[i] = dp[i+1]

print(dp[0])