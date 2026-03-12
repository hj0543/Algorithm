# [로직전략]
# 백트래킹 함수 (dfs)
# 1. 가지치기 : 현재까지의 비용이 이미 구한 최소 비용 이상이면 더 이상 탐색하지 않고 return
# 2. 종료조건 : N개의 제품에 대한 공장 배정이 모두 끝났다면 최소 비용을 갱신하고 return
# 3. 탐색 : 아직 배정되지 않은 공장(visited 체크)에 대해 배정 후 다음 제품(row+1)으로 재귀 호출, 이후 상태 복구(백트래킹)
 
def dfs(row, current_cost):
    global min_cost
     
    # 1. 가지치기
    if current_cost >= min_cost:
        return
         
    # 2. 종료조건
    if row == N:
        min_cost = current_cost
        return
         
    # 3. 공장 탐색 및 배정 (백트래킹)
    for col in range(N):
        if not visited[col]:
            visited[col] = 1
            dfs(row + 1, current_cost + cost[row][col])
            visited[col] = 0 # 상태 복구
 
TC = int(input())
for tc in range(TC):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
     
    visited = [0] * N
    min_cost = float('inf')
     
    dfs(0, 0)
     
    print(f'#{tc+1} {min_cost}')