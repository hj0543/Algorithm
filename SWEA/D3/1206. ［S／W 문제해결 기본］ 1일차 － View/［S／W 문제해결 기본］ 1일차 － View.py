def max_number(x_list):

    max_num = x_list[0]

    for i in range(4):
        if x_list[i] > max_num:
            max_num = x_list[i]
    return max_num

for n in range(10):
    N = int(input())
    height = list(map(int, input().split()))

    total_gap = 0

    for i in range(2, N-2):

        comp = [height[i-2], height[i-1], height[i+1], height[i+2]]


        if height[i] - max_number(comp) > 0:
            total_gap += height[i] - max_number(comp)


    print(f'#{n+1} {total_gap}')