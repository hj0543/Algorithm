import sys
sys.stdin = open('input.txt', 'r')

A, B = map(int, input().split())

for i in range(A, B + 1):
    if i < 2: # 1은 소수가 아니니까 제외
        continue

    prime_number = [] # 빈 소수 list 생성
    for j in range(1, B + 1):
        if i % j == 0: # 나눴을 때 나머지가 없으면 소수 list에 append한다.
            prime_number.append(j)

    if len(prime_number) == 2: # 약수의 개수가 2개면 출력
        print(i)


