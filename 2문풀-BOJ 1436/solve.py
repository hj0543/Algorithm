import sys
sys.stdin = open('input.txt', 'r')

# 7568
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = []
for i in range(M):
    line = list(map(str, input().rstrip()))
    matrix.append(line)
print(matrix)