import sys
input = sys.stdin.readline

# 나보다 왼쪽 탑이 나의 신호를 못받는다?
# 나보다 오른쪽에 있는 탑의 신호도 못받을것이다 -> 제거해서 시간줄이기

N = int(input())
height = list(map(int, input().split()))

stack = [] # 현재 위치보다 키 큰 탑들만 모아둘거임
# (0, 6)의 형태로 들어감 (탑의 위치, 탑의 높이)
result = [0] * N # 번호를 넣을 탑의 개수만큼 빈 리스트 생성

for i in range(N): # 오른쪽에 있는 타워
    while stack:
        # 스택의 top에 있는 탑의 높이가 현재 탑보다 높다면? (수신 가능)
        if stack[-1][1] > height[i]: # stack[-1][1] -> 탑의 높이
            result[i] = stack[-1][0] + 1 # stack[-1][0] -> 탑의 위치
            break
        else:
            # 내 뒤에 올 탑들의 신호도 나한테 가로막혀서 절대 받을 수 없음
            # 즉 -> 현재 탑보다 낮으면 앞으로도 쓸모 없으니 제거
            stack.pop()

        # 현재 탑을 스택에 추가
    stack.append((i, height[i]))

print(' '.join(map(str, result)))