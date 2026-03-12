TC = int(input())
for tc in range(TC):
    a, b, c = map(int, input().split())
    result = 0

    if b >= c:
        reduction = b - (c - 1)
        result += reduction
        b = c - 1

    if a >= b:
        reduction = a - (b - 1)
        result += reduction
        a = b - 1

    if a <= 0 or b <= 0 or c <= 0:
        print(f'#{tc+1} -1')
    else:
        print(f'#{tc+1} {result}')