import sys
sys.stdin = open('input.txt', 'r')

def factorial(a): # 팩토리얼 함수
    fact = 1
    for i in range(1, a + 1):
        fact *= i
    return fact

 # 조합 = M!/ (M-m)! * m!

def comb(x, y): # 조합 함수 (x < y)
    result = factorial(y)/(factorial(y - x) * factorial(x))    
    return result


T = int(input())


for i in range(T):
    N, M = list(map(int, input().split())) # N <= M

    if N == M:
        print(1)
    else:
        print(int(comb(N, M)))
