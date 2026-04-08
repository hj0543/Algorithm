import sys
sys.stdin = open("input.txt", "r")

# SWEA 4008
# 환경 부담 세율(E)과 각 해저터널 길이(L)의 제곱의 곱(E * L^2)만큼 지불

def enviromental_fee(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return False

    parent[b] = a
    return True


# ---------------------------------------------

# 입력 및 실행

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    op_numbers = list(map(int, input().split()))
    numbers = list(map(int, input().split()))


