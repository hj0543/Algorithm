# queue 안쓰고 테스트용

import sys
input = sys.stdin.readline

n = int(input())
move = [0] + list(map(int, input().split()))

left = [0] * (n + 1)
right = [0] * (n + 1)

for i in range(1, n + 1):
    left[i] = i - 1 if i > 1 else n
    right[i] = i + 1 if i < n else 1

result = []
cur = 1

for _ in range(n):
    result.append(cur)
    step = move[cur]

    if len(result) == n:
        break

    l = left[cur]
    r = right[cur]
    right[l] = r
    left[r] = l

    if step > 0:
        nxt = r
        for _ in range(step - 1):
            nxt = right[nxt]
    else:
        nxt = l
        for _ in range(-step - 1):
            nxt = left[nxt]

    cur = nxt

print(*result)
