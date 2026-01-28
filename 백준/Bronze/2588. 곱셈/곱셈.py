num1 = int(input())
num2 = input()  # 두 번째 숫자를 문자열로 받음

# 문자열 인덱싱을 이용해 각 자릿수와 곱셈
print(num1 * int(num2[2]))  # (3)번: 일의 자리 (5)
print(num1 * int(num2[1]))  # (4)번: 십의 자리 (8)
print(num1 * int(num2[0]))  # (5)번: 백의 자리 (3)
print(num1 * int(num2))     # (6)번: 전체 결과