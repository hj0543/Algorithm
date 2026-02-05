N = int(input())

measure = []

for i in range(1, N + 1):
    if N % i == 0:
        measure.append(i)
for j in measure:
    print(f'{j}(은)는 {N}의 약수입니다.')
    
if measure[1] == measure[-1]:
    print(f'{N}(은)는 1과 {j}로만 나눌 수 있는 소수입니다.')