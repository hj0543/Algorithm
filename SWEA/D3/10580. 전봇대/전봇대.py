# 문제풀이 1 - 전봇대

# [로직전략]
# 1. 왼쪽 전봇대 위치 기준으로 오름차순 정렬(lambda 사용)
# 2. 2중 for문으로 오른쪽 높이 비교
# [예외생각]
# 1. 세 전선의 교점이 하나라면? -> 문제조건: 세 전선의 교점은 없다.

TC = int(input())
for tc in range(TC):
    n = int(input())

    line = []
    for _ in range(n):
        line.append(list(map(int, input().split())))

    # 1. 왼쪽 전봇대 기준으로 오름차순 정렬
    line.sort(key=lambda x: x[0])

    # 2. 2중 for문으로 오른쪽 높이비교로 교점 개수 구하기
    counts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if line[i][1] > line[j][1]:
                counts += 1

    print(f'#{tc+1} {counts}')