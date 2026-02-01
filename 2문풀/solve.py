import sys
sys.stdin = open('input.txt', 'r')

# 13909
import sys
input = sys.stdin.readline
N = int(input())

# 메모리 초과 해결을 위한 원리탐색

# 총 합이 홀수이다.
# N번 창문을 연 사람은 N의 약수들이다.
# 약수가 홀수가 되려면 어떤 수의 제곱이여야 하니까
# 제곱근? -> 제곱근을 구해야하니 뒷자리는 잘라도 되니까 정수로 선언하기

print(int(N ** 0.5))



'''
[메모리 초과]

window = [0] * (N + 1) # 창문의 개수 초기값 : 0 -> 닫힘

total = 0


for i in range(1, N + 1): # 1이상 N이하인 수 중에서
    num = N // i # N을 i로 몫나눈값 만큼 배수의 개수가 존재한다.

    for j in range(1, num + 1):

        window[i * j] += 1 # 각 배수의 자리에 1씩 더해준다.

    
    if window[i] % 2 != 0: # 창문을 작동한 횟수가 홀수라면 열려있으니 총 개수에 1을 더한다.
        total += 1
'''


 

