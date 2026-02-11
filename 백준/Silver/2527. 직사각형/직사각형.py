for tc in range(4):
    square = list(map(int, input().split()))
    x1, y1, x2, y2, x3, y3, x4, y4 = square

    # 아예 안 만나는 경우
    if x2 < x3 or x4 < x1 or y2 < y3 or y4 < y1:
        print('d')

    # 점으로 만나는 경우
    elif (x2 == x3 and y2 == y3) or (x2 == x3 and y1 == y4) or \
            (x1 == x4 and y2 == y3) or (x1 == x4 and y1 == y4):
        print('c')

    # 선으로 만나는 경우 - x축이나 y축 중 하나가 맞닿아 있을 때
    elif x1 == x4 or x2 == x3 or y1 == y4 or y2 == y3:
        print('b')

    # 겹치는 부분이 면인 경우
    else:
        print('a')