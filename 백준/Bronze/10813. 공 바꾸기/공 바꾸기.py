N, M = map(int, input().split())

basket = list(range(1, N + 1))


for _ in range(M):
    i, j = map(int, input().split())

    a = basket[i-1] # a에 i번 basket 공을 복사하고
    b = basket[j-1] # b에 j번 basket 공을 복사하고
    c = a # a를 c에 잠시 담아놓고
    basket[i-1] = b # i번 basket에 j번 basket의 공을 넣고
    basket[j-1] = c # j번 basket에 i번 basket의 공을 넣는다.


print(*basket)