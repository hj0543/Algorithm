import sys
sys.stdin = open('input.txt', 'r')

##################################################

TC = int(input())

for tc in range(TC):
    N = int(input())

    road = []
    for _ in range(N):
        road.append(list(map(int, input().split())))

    print(road)



    # print(f'#{tc+1} {total}')