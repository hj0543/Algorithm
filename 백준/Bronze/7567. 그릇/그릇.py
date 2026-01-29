import sys
input = sys.stdin.readline

# 입력이 (())라면 S는 ['(', '(', ')', ')', '\n']이 됩니다.
# 마지막에 있는 \n까지 반복문을 돌면서 이전 문자인 )와 비교하게 되어, 원치 않는 점수(+10)가 합산됩니다.
# .strip()을 사용하여 양 끝의 공백과 개행 문자를 제거해야 합니다.

S = list(input().strip())


# ( 바로    ) 거꾸로 


 # 처음은 무조건 10, i == i - 1 이면 +5 / i != i - 1 이면 +10



total = 10 # S[0] = 10 초기값 설정

for i in range(1, len(S)):
    if S[i] == S[i - 1]:
        total += 5
    else:
        total += 10

print(total)