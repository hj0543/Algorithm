# [로직 설계]
# 1. 특정 좌표 시작
# 2. 6번 이동
# 2-1. 모두 이어붙이자 (문자열이 좋아보인다)
# 2-2. 중복이동 가능하다
# 3. 7자리 수 중복제거 (set)

# 델타배열
# 숫자를 누적하면서 다음으로 이동 -> 6번 반복
# BFS, DFS 가능

# DFS
# 숫자를 누적하면서 이동
# 숫자가 7자리가 되면 종료
# 한 번의 시점에서 나올 수 있는 경우의 수 -> 4가지 (상하좌우)



# DFS버전
# 종료조건 : 숫자가 7자리가 되면 종료
# 가지의 수 : 4가지(상하좌우)


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def recur(y, x, number):
    if number == 7:
        result.add(number)
        return
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        # 범위 밖 체크
        if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
            continue

        recur(ny, nx, number + matrix[ny][nx])


T = int(input())
for tc in range(1, T + 1):
    # 숫자를 이어붙일거라 문자열로 입력
    matrix = [input().split() for _ in range(4)]
    # print(matrix)
    
    result = set()
    # 특정 좌표로부터 출발해서 7자리를 만들자
    for i in range(4):
        for j in range(4):
            recur()










