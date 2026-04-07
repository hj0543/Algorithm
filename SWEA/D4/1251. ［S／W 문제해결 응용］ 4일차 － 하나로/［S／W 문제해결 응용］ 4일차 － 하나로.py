# SWEA 1251
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
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    
    islands = list(zip(X, Y))
    # print(islands)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = islands[i]
            x2, y2 = islands[j]
            edges.append((i, j, enviromental_fee(x1, y1, x2, y2)))

    edges.sort(key=lambda x: x[2])

    result = 0
    counts = 0
    parent = [i for i in range(n)]

    for a, b, w in edges:
        if union(a, b):
            result += w
            counts += 1

        if counts == n - 1:
            break

    print(f'#{tc} {round(result * E)}')