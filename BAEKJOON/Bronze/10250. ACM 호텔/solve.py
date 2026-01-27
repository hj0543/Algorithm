N = int(input())

for _ in range(1, N + 1):
    H, W, N = list(map(int, input().split()))

    line = str(N // H + 1) # 호수

    if N % H == 0:
        floor = H
        line = str(N // H)
    else:
        floor = str(N % H)
        line = str(N // H + 1) # 층수

    if floor == '0':
        print(int(floor), int(line), sep = '0')
    else:
        print(int(floor) * 100 + int(line))