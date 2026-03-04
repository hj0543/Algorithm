import sys

sys.setrecursionlimit(10**5)

def input():
    return sys.stdin.readline().strip()

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]

# DFS 함수 정의
def dfs(x, y):
    # 범위를 벗어났거나, 이미 방문했던 칸이라면 탐색 중지
    if x >= N or y >= N or visited[x][y]:
        return
    
    # 현재 칸을 방문했다고 표시
    visited[x][y] = True
    
    # 목표 지점(-1)에 도달했다면 더 이상 점프할 필요가 없으므로 탐색 중지
    if board[x][y] == -1:
        return
        
    # 현재 칸에서 이동할 거리
    step = board[x][y]
    
    # 다음 경로 탐색
    dfs(x + step, y)
    dfs(x, y + step)

# 출발점(0, 0)
dfs(0, 0)

# 끝점 (N-1, N-1)을 방문한 적이 있다면 도달
if visited[N-1][N-1]:
    print("HaruHaru")
else:
    print("Hing")