import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    print(f'Case #{i + 1}: {A + B}')

    # for n in range(1, T):
    #     print(f'Case #{n}: {A + B}')
    #     break

    # 출력
    '''
    Case #1: 2
    Case #1: 5
    Case #1: 7
    Case #1: 17
    Case #1: 7
    '''