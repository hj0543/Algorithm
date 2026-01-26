import sys
sys.stdin = open('input.txt', 'r')

A, B = map(int, input().split())

for i in range(A, B + 1):
    if i < 2: # 1은 소수가 아니니까 제외
        continue

    is_prime = True # 소수라고 가정
    for j in range(2, int(i ** 0.5) + 1): # 2부터 수의 제곱근만큼만 곱해도 됨
        if i % j == 0: # i를 j로 나누었을 때 나머지가 0이면 소수가 아님(본인 수가 아니기 때문)
            is_prime = False # 그럼 소수가 아님
            break # 소수가 아니니까 반복문 탈출

    if is_prime == True: # 소수면 i 출력한다. (if is_prime: 으로 나타내도 된다고 함)
        print(i)


