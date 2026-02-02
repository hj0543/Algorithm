T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    new_list = []


    for j in range(N - M + 1):
        temp = 0
        for k in range(M):
            temp += numbers[j+k]

        new_list.append(temp)

    max_num = new_list[0]
    min_num = new_list[0]

    for j in range(N - M + 1):
        if new_list[j] > max_num:
            max_num = new_list[j]

        if new_list[j] < min_num:
            min_num = new_list[j]

    result = max_num - min_num

    print(f'#{i+1} {result}')