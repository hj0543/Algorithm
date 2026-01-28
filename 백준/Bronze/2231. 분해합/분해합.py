N = int(input())

result = 0 # 기본값 설정 (생성자가 없는 경우에는 0을 출력한다.)

for i in range(1, N + 1):
    number = i + sum(map(int, str(i))) # 분해합은 원래 수 + 각자리 수 
    if number == N: # 같다면 number는 생성자 이니까
        result = i
        break

print(result)
