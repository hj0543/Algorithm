import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

stack = []

current = 1 # 현재 간식 받아야하는 번호표

for student in numbers:
    stack.append(student)   # 대기열에 넣고

    while stack and stack[-1] == current:   # 대기열의 맨 위 학생이 현재 순서라면
        stack.pop()     # 간식주고 빼고
        current += 1    # 번호표 다음 사람

if not stack:
    print('Nice')
else:
    print('Sad')