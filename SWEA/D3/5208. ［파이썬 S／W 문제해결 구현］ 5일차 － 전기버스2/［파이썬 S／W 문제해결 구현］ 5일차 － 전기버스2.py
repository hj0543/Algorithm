# [로직전략]
# 백트래킹 함수
# 1. 가지치기 : 현재 교체 횟수가 이미 구한 최솟값 이상이면 return
# 2. 종료조건 : 목적지 도착
# 3. 현재 정류장에서 충전된 배터리 용량만큼 최대한 멀리 가는 경우부터 이동 가능한 정류장 탐색 (역순 탐색)

def dfs(idx, cnt):
    global min_cnt
    
    # 가지치기
    if cnt >= min_cnt:
        return
        
    # 종료조건
    if idx >= N:
        min_cnt = cnt
        return
        
    for i in range(battery[idx], 0, -1):
        dfs(idx + i, cnt + 1)

TC = int(input())
for tc in range(TC):
    data = list(map(int, input().split()))
    N = data[0]
    battery = [0] + data[1:] 
    
    min_cnt = float('inf')
    # 1번 정류장에서 출발 (출발할 때 장착된 배터리는 교체 횟수에 포함하지 않으므로 -1로 시작)
    dfs(1, -1)
    
    print(f'#{tc+1} {min_cnt}')