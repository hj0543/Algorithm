# 정수 N 입력
N = int(input())

# 1부터 N까지 반복
for i in range(1, N + 1):
    # i번만큼 별을 반복해서 출력 (예: i가 3이면 '***')
    print('*' * i)