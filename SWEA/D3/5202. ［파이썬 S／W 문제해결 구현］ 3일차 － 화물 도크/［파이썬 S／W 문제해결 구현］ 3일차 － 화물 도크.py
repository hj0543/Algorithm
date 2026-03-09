
TC = int(input())

for tc in range(TC):
    N = int(input())
    tasks = []
    for _ in range(N):
        tasks.append(list(map(int, input().split())))

    tasks.sort(key=lambda x: (x[1], x[0]))

    counts = 0
    last_end_time = 0 # 마지막 작업이 끝난 시간

    for start, end in tasks:
        if start >= last_end_time:
            counts += 1
            last_end_time = end

    print(f"#{tc+1} {counts}")