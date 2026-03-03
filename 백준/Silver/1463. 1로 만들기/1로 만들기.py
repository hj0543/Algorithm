import sys
input = sys.stdin.readline

n = int(input())

# dp[i]는 숫자 i를 1로 만드는 최소 연산 횟수
dp = [0] * (n + 1)

for i in range(2, n + 1):
    # 1을 빼는 경우를 먼저 고려
    dp[i] = dp[i - 1] + 1

    # 2로 나누어 떨어지고, 2로 나누는 게 더 빠르면 갱신
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    # 3으로 나누어 떨어지고, 3으로 나누는 게 더 빠르면 갱신
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[n])