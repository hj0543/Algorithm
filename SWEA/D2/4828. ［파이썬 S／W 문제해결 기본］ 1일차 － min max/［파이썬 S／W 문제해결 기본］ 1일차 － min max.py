

T = int(input())



for i in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))

    max_num = numbers[0]
    min_num = numbers[0]

    for j in range(1, N):
        if numbers[j] > max_num:
            max_num = numbers[j]

    for j in range(1, N):
        if numbers[j] < min_num:
            min_num = numbers[j]

    result = max_num - min_num

    print(f'#{i+1} {result}')