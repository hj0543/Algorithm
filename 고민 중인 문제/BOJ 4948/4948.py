'''
시간초과 해결법 고민중
'''

import sys
sys.stdin = open('input.txt', 'r')

# 4948
import sys
input = sys.stdin.readline

##################################################################

import math

def is_prime(n):
    if n < 2:
        return False
    # 2부터 n의 제곱근까지 나누어 봄
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False # 소수가 아님
    return True # 소수임


# def is_prime_simple(n):
#     if n < 2: 
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

########################################################################

while True:
    n = int(input())
    if n == 0:
        break

    cnt = 0 # 소수의 개수 초기값 0 설정


    for i in range(n + 1, (2 * n) + 1): # 임의의 정수 i가 초과 2n미만의 범위에서
        if is_prime(i) == True: # i가 소수라면
            cnt += 1 # 카운트를 한다.
        else: # 아니면 패스
            pass


    print(cnt)


    

