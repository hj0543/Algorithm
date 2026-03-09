n, m = map(int, input().split())
result = [0] * m

def backtracking(depth):
    if depth == m:
        print(*result, sep = ' ')
        return

    for i in range(1, n + 1):
        result[depth] = i
        backtracking(depth + 1)

backtracking(0)