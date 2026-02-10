import sys
sys.stdin = open('input.txt', 'r')

##################################################


def dfs(arr, v):
    visited[v] = True
    for w in arr[v]:
        if visited[w] != True:
            dfs(arr, w)


TC = int(input())

for tc in range(TC):
    E = int(input())

    # 인접 리스트 요소 받기

    data = list(map(int, input().split()))


    # 인접리스트 요소
    arr = [[] for _ in range(100 + 1)]
    visited = [0] * (100 + 1)


    for i in range(E):  # 간선의 개수만큼 돌아야함
        s, e = data[2 * i], data[2 * i + 1]  # 인덱스 2개씩 쌍으로 받기 위해서 (1, 2) (1, 3) (2, 4)...
        arr[s].append(e)


    dfs(arr, 0)

    if visited[99] == True:
        print(f'#{tc+1} 1')
    else:
        print(f'#{tc+1} 0')