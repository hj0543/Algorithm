import sys
sys.stdin = open('input.txt', 'r')

##################################################
# 4837 부분집합의 합

# [로직전략]
# 1.

def dfs_subset(depth):
    # 종료조건
    if depth == n:
        subset = [A[i] for i in range(n) if visited[i]]
        return

    # 현재 원소 포함
    visited[depth] = True
    dfs_subset(depth + 1)

    # 현재 원소 미포함
    visited[depth] = False
    dfs_subset(depth + 1)

TC = int(input())
for tc in range(TC):
    N, K = map(int, input().split())
    A = [i for i in range(1, 13)]
    n = len(A)
    visited = [False] * n
    print(dfs_subset(0))
