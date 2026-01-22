import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

for i in range(1, N + 1):
    print(f"{'*' * i:>{N}}")


'''
이거는 왜 안되는지 모르겠음 -> 출력 오류
N = int(input())

for i in range(N + 1):
    print(' '*(N - i) + '*' * i)
'''
