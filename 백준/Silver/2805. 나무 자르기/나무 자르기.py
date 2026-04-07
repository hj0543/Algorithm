import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

left, right = 0, max(trees)
answer = 0

while left <= right:
    mid = (left + right) // 2
    total = 0

    for t in trees:
        if t > mid:
            total += (t - mid)

    if total >= m:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)