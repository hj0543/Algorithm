import sys
sys.stdin = open('input.txt', 'r')

##################################################
# 15652
# [기존 로직전략] -> 시간초과
# 1. backtracking 함수의 변수에 depth만 넣고 조건문을 통해 대소비교를 만족하지 않으면 출력하지 않음.
# 2. 종료조건 - 4 4 를 출력
# 3. 출력 후 재귀함수를 통해 종료 조건이 될 때 까지 반복시킴.

# [수정 로직전략]
# 1. 시작지점을 함수 변수에 넣어 for문을 통해 인덱스 접근으로 시작점을 1씩 늘려나감.
# 2. 언패킹하여 바로 출력

n, m = map(int, input().split())
result = [0] * m

def backtracking(depth, start):
    if depth == m:
        print(*result)
        return

    for i in range(start, n + 1):
        result[depth] = i
        backtracking(depth + 1, i)

backtracking(0, 1)

'''
def backtracking(depth):
    if depth == m:
        check = 1
        for i in range(1, m):
            if result[i - 1] <= result[i]:
                check += 1
        if check == m:
            print(*result, sep = ' ')
        return

    for i in range(1, n + 1):
        result[depth] = i
        backtracking(depth + 1)

backtracking(0)
'''