# 두 정수 A와 B를 입력받아 공백으로 분리하고 정수로 변환
A, B = map(int, input().split())

# 조건문을 통한 비교 및 출력
if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')
   