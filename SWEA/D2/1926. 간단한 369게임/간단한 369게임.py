N = int(input())

for i in range(1, N+1):
    curr = str(i)
    # 3, 6, 9가 몇 번 나오는지 카운트
    count = curr.count('3') + curr.count('6') + curr.count('9')

    if count > 0:
        # 박수 횟수만큼 '-' 출력
        print("-" * count, end=" ")
    else:
        # 3, 6, 9가 없으면 숫자 그대로 출력
        print(i, end=" ")