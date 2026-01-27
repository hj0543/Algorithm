while True:
    nums = list(map(int, input().split()))

    if sum(nums) == 0:
        break

    a, b, c = nums[0], nums[1], nums[-1]

    if a ** 2 + b ** 2 == c ** 2:
        print('right')
    elif b ** 2 + c ** 2 == a ** 2:
        print('right')
    elif a ** 2 + c ** 2 == b ** 2:
        print('right')
    else:
        print('wrong')