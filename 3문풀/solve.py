import sys
sys.stdin = open('input.txt', 'r')

# 11653
import sys
input = sys.stdin.readline
N = int(input())

d = 2 # 소인수분해 최소 2로 나누기때문에 초기값 2

# prime = [] # 소인수분해 한 소수들 들어갈 리스트

while N > 1: # 나누는 수가  N 몫나눗셈 2 작을동안 실행
    if (N % d) == 0: # N을 d로 나눴을 때 0이면
        print(d)
        N /= d

    else:
        d += 1          # 

# for j in range(len(prime)):
#     print(j)


# 72 -> 36 -> 18 -> 9 -> 3 -> 1
