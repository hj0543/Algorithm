import sys
sys.stdin = open('input.txt', 'r')

##################################################
# 15652
n, m = map(int, input().split())
result = [0] * m

def backtracking(depth):
    if depth == m:
        # check = 1
        # for i in range(1, m):
        #     if result[i - 1] <= result[i]:
        #         check += 1
        # if check == m:
        #     print(*result, sep = ' ')
        return

    for i in range(1, n + 1):
        result[depth] = i
        backtracking(depth + 1)

backtracking(0)


