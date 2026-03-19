import sys
input = sys.stdin.readline

def backtracking(depth, start):
    global min_diff

    # 가지치기
    if min_diff == 0 or depth > N // 2 or start >= N:
        return

    # 팀이 절반으로 나뉘었을 때 점수차 계산
    if depth == N // 2:
        start_team = []
        link_team = []

        # 팀 구성하기
        for i in range(N):
            if visited[i]:
                start_team.append(i)
            else:
                link_team.append(i)

        start_score = 0
        link_score = 0

        # 팀 내 점수 계산
        for i in range(N // 2):
            for j in range(i + 1, N // 2):
                start_score += S[start_team[i]][start_team[j]] + S[start_team[j]][start_team[i]]
                link_score += S[link_team[i]][link_team[j]] + S[link_team[j]][link_team[i]]

        # 최소점수차 갱신
        min_diff = min(min_diff, abs(start_score - link_score))
        return

    # 다음 경우
    for i in range(start, N):
        if not visited[i]:
            visited[i] = True
            backtracking(depth + 1, i + 1)
            visited[i] = False

# --------------------------------------------------------

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N

min_diff = int(1e9)
backtracking(0, 0)

print(min_diff)