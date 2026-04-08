import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

result = [set() for _ in range(N + 1)]

for i in range(1, N + 1):
    data = list(map(int, input().split()))
    k = data[0]
    result[i] = set(data[1:])

out = []

for _ in range(Q):
    cmd, a, *rest = map(int, input().split())
    
    # 집합 Sa를 Sa ∪ Sb로 바꾸고, Sb는 공집합으로 바꾼다.
    if cmd == 1:
        b = rest[0]

        if len(result[a]) < len(result[b]):
            result[a], result[b] = result[b], result[a]

        result[a].update(result[b])
        result[b].clear()
    
    # 집합 Sa의 크기를 출력한다.
    else:
        out.append(str(len(result[a])))

for ans in out:
    print(ans)