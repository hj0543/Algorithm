T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    coordinates = [tuple(map(int, input().split())) for _ in range(N)]

    # x_range[x] = x좌표가 x인 점들의 y 최솟값, y 최댓값
    # y_range[y] = y좌표가 y인 점들의 x 최솟값, x 최댓값
    x_range = {}
    y_range = {}

    # 한 점을 직각 꼭짓점으로 잡았을 때, 같은 x / 같은 y에 있는 가장 먼 점만 알면 된다.
    for x, y in coordinates: # 직각 꼭지점 임의로 잡은거임

        # 같은 x좌표에 있는 점들 중 y의 범위를 저장한다.
        # 이 범위에서 현재 점과 가장 먼 y거리가 삼각형의 세로 길이가 된다.
        if x not in x_range:
            x_range[x] = [y, y] # 임시로 최소, 최대 초기설정을 하는 거임
        else:	# 이미 x가 존재하면 초기설정 값이 들어가 있으니까 최소와 최대를 갱신
            x_range[x][0] = min(x_range[x][0], y)
            x_range[x][1] = max(x_range[x][1], y)

        # 같은 y좌표에 있는 점들 중 x의 범위를 저장한다.
        # 이 범위에서 현재 점과 가장 먼 x거리가 삼각형의 가로 길이가 된다.
        if y not in y_range:
            y_range[y] = [x, x] # 임시로 최소, 최대 초기설정을 하는 거임
        else:	# 이미 y가 존재하면 초기설정 값이 들어가 있으니까 최소와 최대를 갱신
            y_range[y][0] = min(y_range[y][0], x)
            y_range[y][1] = max(y_range[y][1], x)

    max_area = 0

    for x, y in coordinates:
        # 현재 점 (x, y)를 직각 꼭짓점으로 생각한다.
        min_y, max_y = x_range[x]
        min_x, max_x = y_range[y]

        height = max(abs(y - min_y), abs(max_y - y))
        width = max(abs(x - min_x), abs(max_x - x))

        max_area = max(max_area, width * height)

    print(max_area)