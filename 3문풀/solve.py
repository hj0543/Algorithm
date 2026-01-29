import sys
sys.stdin = open('input.txt', 'r')

# 4948
import sys
input = sys.stdin.readline


while True:
    n = int(input())
    if n == 0:
        break

    cnt = 0



for i in range(n, (n * 2) + 1):
    
    for j in range(n + 1, ((n * 2) + 1) // 2):
        if i % j != 0:
            cnt += 1


    print(cnt)