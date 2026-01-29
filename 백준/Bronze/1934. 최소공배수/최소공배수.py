import math
import sys

input = sys.stdin.readline
T = int(input())


for _ in range(T):
    AB = list(map(int, input().split()))
    A, B = AB[0], AB[1]


    G = math.gcd(A, B) # 최대공약수 구하는 math 함수

    L = A * B // G # 최소공배수는 '두 수의 곱 / 최대공약수' 니까
    # i_list = [] # 소인수분해 된 수들을 담을 빈 lsit

    
    

    # if a == 1 and b == 1:
    #     i_list.append(1)

    # else:
    #     i = 2 # 소인수분해 할 초기값 설정 2
    #     while i <= min(AB):
    #         if a % i == 0 and b % i == 0:
    #             i_list.append(i) # 소인수분해 된 값들을 i_list에 담는다
                
    #             # 담고 그 수로 나눈다.
    #             a = a // i 
    #             b = b // i
    #         else:
    #             i += 1 # 안나눠지면 1을 더해서 다시 나눠봐야지
    # # [], [2], []

     
    # if len(i_list) == 0:
    #     print(AB[0] * AB[1]) # 약수가 없으면 작은 값이 최대공약수다.
    # else:
    #     total = 1 # 소인수분해 한 소수들의 곱 초기값 1(즉, 최대공약수)
    # #     for j in range(len(i_list)):
    # #         total *= i_list[j] # 최대공약수 만들기

    #     print((AB[0] * AB[1]) // total) # 최소공배수는 '두 수의 곱 / 최대공약수' 니까


    print(L)
