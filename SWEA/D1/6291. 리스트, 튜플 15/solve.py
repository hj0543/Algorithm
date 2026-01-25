import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

dan = [f'{N} * {n} = {N * n}' for n in range(1, 10)]

print(dan, end = ' ')

words = input()
if words == '종료':
    print('프로그램을 종료합니다.')


    