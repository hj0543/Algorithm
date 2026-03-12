import sys; sys.stdin = open('BOJ_2048.txt')
from itertools import product
from copy import deepcopy

# 특정 방향(idx)으로 블록들을 이동시키고 합치는 함수
def delta(idx, val):
    global arr
    # 이동 방향 벡터: 0:상(-1,0), 1:하(1,0), 2:좌(0,-1), 3:우(0,1)
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
    # 한 번의 이동(한 턴)에서 이미 합쳐진 블록인지 체크 (2+2=4가 된 직후 또 4와 합쳐지는 것 방지)
    used = [[False] * n for _ in range(n)]

    # 격자의 모든 칸을 순회하며 블록 이동 처리
    for row in range(n):
        for col in range(n):
            if c_arr[row][col] != 0: # 현재 칸에 블록(숫자)이 있을 때만 실행
                
                # k는 현재 위치에서 '얼마나 멀리' 이동할지를 결정 (1칸부터 최대 n-1칸까지)
                for k in range(1, n):
                    # nx, ny: 현재 방향으로 k만큼 전진했을 때의 '도착 후보' 좌표
                    nx = row + direction[idx][0] * k
                    # prev_nx, prev_ny: nx, ny보다 딱 한 칸 뒤(방금 지나온 칸)의 좌표
                    prev_nx = row + direction[idx][0] * (k-1)
                    ny = col + direction[idx][1] * k
                    prev_ny = col + direction[idx][1] * (k-1)
                    
                    # 1. 이동할 위치(nx, ny)와 그 직전 위치(prev)가 모두 격자 범위 안인지 확인
                    if 0 <= nx < n and 0 <= ny < n and 0 <= prev_nx < n and 0 <= prev_ny < n:
                        
                        # Case A: 이동할 곳에 나랑 똑같은 숫자가 있고, 아직 합쳐진 적 없는 블록이라면?
                        if c_arr[row][col] == c_arr[nx][ny] and not used[nx][ny]:
                            c_arr[row][col] = 0      # 원래 있던 자리는 비우고
                            c_arr[nx][ny] *= 2       # 도착지 숫자를 2배로 (합치기)
                            used[nx][ny] = True      # 합쳐졌음을 표시
                            
                            # 현재 판에서 가장 큰 블록 값(val) 업데이트
                            if c_arr[nx][ny] >= val:
                                val = c_arr[nx][ny]
                        
                        # Case B: 이동할 곳이 빈칸이 아니고(숫자가 있고), 나랑 다른 숫자라면? (더 못 감)
                        elif c_arr[nx][ny] not in [0, c_arr[row][col]]:
                            # 장애물 바로 전 칸(prev)에 현재 블록을 배치
                            c_arr[prev_nx][prev_ny] = c_arr[row][col]
                            # 만약 원래 자리와 이동한 자리가 다르다면 원래 자리는 비움
                            if not (prev_nx == row and prev_ny == col):
                                c_arr[row][col] = 0
                            break # 더 이상 전진할 수 없으므로 k 루프 중단
                    else:
                        # 격자 범위를 벗어나려고 하면, 직전 위치(벽 끝)에 멈춤 처리 로직이 필요함
                        pass 
    return val

# 5번의 이동 조합을 재귀적으로 실행하는 함수
def DFS(direct, val, cnt):
    # 5번 이동이 완료되면 최종 최대값 반환
    if cnt == 5:
        return val

    # direct 리스트에 담긴 방향 순서대로 이동 (1:상, 2:하, 3:좌, 4:우)
    # direct[cnt]-1 로 인덱스를 맞춰 delta의 idx로 전달
    if direct[cnt] == 1:
        return DFS(direct, delta(0, val), cnt + 1)
    elif direct[cnt] == 2:
        return DFS(direct, delta(1, val), cnt + 1)
    elif direct[cnt] == 3:
        return DFS(direct, delta(2, val), cnt + 1)
    elif direct[cnt] == 4:
        return DFS(direct, delta(3, val), cnt + 1)

# --- 메인 실행부 ---
n = int(input()) # 격자 크기
arr = [list(map(int, input().split())) for _ in range(n)] # 초기 상태
direct_lst = [1, 2, 3, 4] 
result = 0

# itertools.product를 사용하여 4가지 방향의 모든 5중 중복 순열 생성 (4^5 = 1024가지 경로)
for permt in product(direct_lst, repeat=5):
    c_arr = deepcopy(arr) # 각 시나리오마다 보드를 원본으로 복사해서 사용
    DFS_result = DFS(list(permt), 0, 0) # 해당 경로로 진행했을 때의 최대값 계산
    
    # 전체 시나리오 중 가장 큰 값 갱신
    if result <= DFS_result:
        result = DFS_result

print(result)