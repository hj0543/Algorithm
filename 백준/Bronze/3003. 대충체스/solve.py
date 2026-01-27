import sys
sys.stdin = open('input.txt', 'r')

N = list(map(int, input().split()))

chess = [1, 1, 2, 2, 2, 8]

for i in range(len(N)):
    compare = chess[i] - N[i]
    print(compare, end = ' ')
    


