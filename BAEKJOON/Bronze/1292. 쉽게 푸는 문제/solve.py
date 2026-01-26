import sys
sys.stdin = open('input.txt', 'r')

A, B = map(int, input().split())

numbers = [] # 수열을 빈 리스트로 생성
for i in range(1, B + 1):
    for j in range(i):
        numbers.append(i)
        if len(numbers) == B:
            break

result = numbers[A - 1 : B] # 범위를 지정하여 슬라이싱

list_result = list(result) # 슬라이싱한 숫자를 다시 리스트로 변환

# 리스트 내 수의 합 구하기
total = 0
for k in (list_result):
    total += int(k)

print(total)
