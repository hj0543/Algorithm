import sys
sys.stdin = open('input.txt', 'r')

##################################################
def enq(n):
    global last
    last += 1
    tree[last] = n

    c = last
    p = c // 2
    while p and tree[p] > tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c//2

TC = int(input())
for tc in range(TC):
    N = int(input())
    arr = list(map(int, input().split()))

    tree = [0] * (N + 1)
    last = 0

    for i in range(N):
        enq(arr[i])

    total = 0
    while True:
        N //= 2
        total += tree[N]
        if N == 0:
            break

    print(f'#{tc+1}', total)