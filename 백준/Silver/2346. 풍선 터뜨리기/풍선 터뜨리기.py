
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
moves = list(map(int, input().split()))

queue = deque()
for i in range(n):
    queue.append((i + 1, moves[i]))

result = []

while queue:
    idx, move = queue.popleft()
    result.append(idx)

    if not queue:
        break

    if move > 0:
        queue.rotate(-(move - 1))
    else:
        queue.rotate(-move)
    
print(*result)



