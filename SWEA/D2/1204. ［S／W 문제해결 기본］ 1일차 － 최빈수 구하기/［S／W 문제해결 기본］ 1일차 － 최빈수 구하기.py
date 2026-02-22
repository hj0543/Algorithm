TC = int(input())

for tc in range(TC):
    tc_num = int(input())
    scores = list(map(int, input().split()))

    re_scores = [0] * 101

    for i in scores:
        re_scores[i] += 1
    value = [i for i, x in enumerate(re_scores) if x == max(re_scores)]

    print(f'#{tc+1} {max(value)}')