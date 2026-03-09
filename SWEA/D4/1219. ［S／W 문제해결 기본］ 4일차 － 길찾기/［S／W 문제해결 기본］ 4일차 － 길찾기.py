def dfs(v):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:
            dfs(w)

for tc in range(10):
    T, E = map(int, input().split())
    V = 100
    temp = list(map(int,input().split()))

    graph = [[] for _ in range(V + 1)]
    visited = [False] * (V + 1)

    for i in range(E):
        s = temp[2*i]
        e = temp[2*i+1]

        graph[s].append(e)

    dfs(1)

    if visited[99] == True:
        print(f'#{tc+1} 1')
    else:
        print(f'#{tc+1} 0')