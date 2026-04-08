T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    pair = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            v = arr[i][j] + arr[j][i]
            pair[i][j] = v
            pair[j][i] = v

    half = N // 2
    chosen = [0]
    selected = [False] * N
    selected[0] = True
    ans = [float('inf')]  # 🔥 여기 수정

    def dfs(start, cnt, sum_a):
        if ans[0] == 0:
            return

        if cnt == half:
            b = []
            for i in range(N):
                if not selected[i]:
                    b.append(i)

            sum_b = 0
            for i in range(half):
                bi = b[i]
                for j in range(i + 1, half):
                    sum_b += pair[bi][b[j]]

            diff = abs(sum_a - sum_b)
            if diff < ans[0]:
                ans[0] = diff
            return

        need = half - cnt
        if N - start < need:
            return

        for x in range(start, N):
            add = 0
            for y in chosen:
                add += pair[x][y]

            chosen.append(x)
            selected[x] = True
            dfs(x + 1, cnt + 1, sum_a + add)
            selected[x] = False
            chosen.pop()

    dfs(1, 1, 0)
    print(f"#{tc} {ans[0]}")