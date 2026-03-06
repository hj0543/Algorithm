import sys
input = sys.stdin.readline

def backtracking(depth):
    if depth == m:
        print(*result)
        return

    for i in range(1, n + 1):
        # 아직 사용하지 않은 숫자라면
        if not visited[i]:
            visited[i] = True  # 방문 표시 (숫자 사용)
            result.append(i)   # 결과 리스트에 추가

            backtracking(depth + 1)   # 다음 숫자 뽑으러 가기 (재귀 호출)

            result.pop()       # 마지막에 넣었던 숫자 제거
            visited[i] = False # 방문 표시 해제 (다른 경로에서 쓸 수 있게 함)

n, m = map(int, input().split())

visited = [False] * (n + 1) # 숫자 사용 여부 체크
result = []                 # 현재까지 만든 수열

backtracking(0)