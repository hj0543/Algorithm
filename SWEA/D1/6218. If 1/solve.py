import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

measure = []

for i in range(1, N + 1):
    if N % i == 0:
        measure.append(i)
for j in measure:
    print(f'{j}(은)는 {N}의 약수입니다.')
