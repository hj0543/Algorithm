import sys
sys.stdin = open('input.txt', 'r')

##################################################

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def dfs(r, c):
    if maze[r][c] == 3:
        return True

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < 16 and 0 <= nc < 16:
            if maze[nr][nc] != 1 and not visited[nr][nc]:
                visited[nr][nc] = True
                if dfs(nr, nc):
                    return True
    return False

for _ in range(10):
    tc = int(input())
    maze = []
    for _ in range(16):
        maze.append(list(map(int,input().rstrip())))

    visited = [[False] * 16 for _ in range(16)]

    r, c = 0, 0
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                r, c = i, j

    if dfs(r, c):
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')