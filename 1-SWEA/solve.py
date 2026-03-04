import sys
sys.stdin = open('input.txt', 'r')

##################################################

number_data = {
    '0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
    '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9
}

TC = int(input())
for tc in range(TC):
    n, m = map(int, input().split())


    found = False   # 암호 찾았니?
    grid = []

    for _ in range(n):
        grid.append(input().rstrip())
    # print(grid)
    nums = []
    for row in grid:
        if not found and '1' in row:
            # 암호의 맨 오른쪽 끝(1) 위치 찾기
            end_idx = row.rfind('1')

            # 끝점에서 앞으로 56칸 잘라내기
            target = row[end_idx - 55: end_idx + 1]

            # 7비트씩 8번 잘라서 숫자로 변환
            for i in range(0, 56, 7):
                number = target[i: i + 7]
                nums.append(number_data[number])

            found = True # 암호 찾음
        if found:
            break

    even_number = nums[1], nums[3], nums[5], nums[7]
    odd_number = nums[0], nums[2], nums[4], nums[6]

    if (sum(odd_number) * 3 + sum(even_number)) % 10 == 0:
        print(f'#{tc+1} {sum(nums)}')
    else:
        print(f'#{tc+1} 0')