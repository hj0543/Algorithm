import sys
sys.stdin = open('input.txt', 'r')

<<<<<<< HEAD
#9095

import sys
input = sys.stdin.readline


# 팩토리얼 함수
def factorial(a): 
    fact = 1
    for i in range(1, a + 1):
        fact *= i
    return fact


# 조합 함수
def comb(a, b, c):
    comb = factorial(a + b + c) // (factorial(a) * factorial(b) * factorial(c))
    return comb

###################################################################################

T = int(input())


for _ in range(T):
    n = int(input())

    
    total = 0 # 각각의 조합의 합 초기값 설정

    for x in range(11): # x의 범위는 0부터 10까지
        for y in range(6): # y의 범위는 0부터 5까지
            for z in range(4): # z의 범위는 0부터 3까지

                if x + (2 * y) + (3 * z) == n: # 곱의 합이 10이라면
                    total += comb(x, y, z) # 그 경우의 조합을 구해서 total에 더함

    print(total)



        


=======
import sys
input = sys.stdin.readline

A, B, N = map(int, input().split())
>>>>>>> 957084cac80be7a80082671b0e152febb4160ddf

# * 10^n n => 5   | 10^n 일의 자리에 해당하는 숫자가 소수 n의 자리가 된다. 


num1 = A * (10 ** N) # A에 10의 N제곱만큼 곱한다.

num2 = num1 // B # num1에서 B의 몫나눗셈을 한다. (소숫점 자를거라서)

result = str(num2)[-1] # 마지막에 있는 수가 소수 N번째 자릿수

print(result)
 







