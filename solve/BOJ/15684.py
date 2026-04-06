# 로직 설계
# 1. board[row][col] = True 이면 row번 가로 위치에서
#    col번 세로선과 col + 1번 세로선이 연결되어 있다고 본다.

# 2. 현재 사다리 상태가 정답인지 확인할 때는,
#    각 세로선 출발점에서 아래로 내려가며 이동을 직접 시뮬레이션한다.
#    현재 위치에서 오른쪽 연결선이 있으면 오른쪽으로,
#    왼쪽 연결선이 있으면 왼쪽으로 이동한다.

# 3. 모든 출발 세로선이 자기 자신 번호로 끝나면 올바른 사다리이다.

# 4. 추가 가능한 가로선 수는 최대 3개이므로,
#    0개일 때 먼저 검사하고 이후 1개, 2개, 3개를 차례대로 백트래킹 탐색한다.

# 5. 가로선은 같은 높이에서 인접하게 놓을 수 없으므로
#    현재 칸, 왼쪽 칸, 오른쪽 칸을 함께 확인한 뒤 놓을 수 있을 때만 진행한다.

# 6. 처음으로 조건을 만족시키는 추가 개수가 정답이고,
#    끝까지 불가능하면 -1을 반환한다.


# 조건을 만족하는지 검사하는 함수
# board[row][col] == True:
# row 높이에서 col 세로선과 col + 1 세로선 사이에 가로선이 존재
def is_valid():
    # 각 세로선을 시작점으로 삼아 아래까지 내려가 본다.
    for start in range(1, n + 1):
        col = start

        # 위에서 아래로 한 줄씩 내려가며 좌우 이동 여부 확인
        for row in range(1, h + 1):
            # 현재 세로선에서 오른쪽으로 연결된 가로선이 있으면 오른쪽 이동
            if board[row][col]:
                col += 1
            # 없고, 왼쪽 세로선에서 현재 세로선으로 연결된 가로선이 있으면 왼쪽 이동
            elif col > 1 and board[row][col - 1]:
                col -= 1

        # 시작 번호와 도착 번호가 다르면 조건 불만족
        if col != start:
            return False

    # 모든 세로선이 자기 자신으로 돌아오면 조건 만족
    return True

# 백트래킹 함수
def dfs(idx, count, target):
    # 종료조건
    # 목표 개수만큼 가로선을 추가했다면 현재 상태를 검사
    if count == target:
        return is_valid()

    # (row, col) 후보를 1차원 인덱스로 순회하여 중복 조합 탐색 방지
    for pos in range(idx, h * (n - 1)):
        row = pos // (n - 1) + 1
        col = pos % (n - 1) + 1

        # 현재 위치에 이미 가로선이 있거나,
        # 같은 높이의 좌우 인접 칸에 가로선이 있으면 놓을 수 없다.
        if board[row][col] or board[row][col - 1] or board[row][col + 1]:
            continue

        # 가로선을 추가하고 다음 경우를 탐색
        board[row][col] = True
        if dfs(pos + 1, count + 1, target):
            return True

        # 실패하면 원상복구 후 다른 위치를 시도
        board[row][col] = False

    return False




# 입력부
n, m, h = map(int, input().split())

# [a, b]는 a번 높이에서 b번 세로선과 b + 1번 세로선을 연결한다는 뜻
lines = [list(map(int, input().split())) for _ in range(m)]


board = [[False] * (n + 1) for _ in range(h + 1)]

# 입력으로 주어진 기존 가로선을 board에 반영
for a, b in lines:
    board[a][b] = True

# 이미 조건을 만족하면 추가 가로선은 0개
if is_valid():
    print(0)
    exit()

# 1개, 2개, 3개 추가하는 경우를 순서대로 시도
for target in range(1, 4):
    if dfs(0, 0, target):
        print(target)
        break
else:
    # 3개 이하로는 만들 수 없는 경우
    print(-1)
