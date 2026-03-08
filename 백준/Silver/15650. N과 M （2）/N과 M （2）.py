import sys

def dfs(start, depth):
    if depth == m:
        print(*result)
        return

    for i in range(start, n + 1):
        result.append(i)
        dfs(i + 1, depth + 1)
        result.pop() # 원상복구

n, m = map(int, sys.stdin.readline().split())
result = []
dfs(1, 0)