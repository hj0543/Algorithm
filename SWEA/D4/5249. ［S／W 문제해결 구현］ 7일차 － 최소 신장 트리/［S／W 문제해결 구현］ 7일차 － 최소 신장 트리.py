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


# ----------------------------------------------

# 입력부

T = int(input())

for tc in range(1, T + 1):
    v, e = map(int, input().split())

    edges = []
    for _ in range(e):
        n1, n2, w = map(int, input().split())
        edges.append((n1, n2, w))

    edges.sort(key=lambda x: x[2])

    parent = [i for i in range(v + 1)]
    result = 0
    count = 0

    for n1, n2, w in edges:
        if union(n1, n2):
            result += w
            count += 1

        if count == v:
            break

    print(f"#{tc} {result}")