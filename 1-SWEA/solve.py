import sys
sys.stdin = open('input.txt', 'r')

##################################################

# 16진수 -> 2진수 변환 딕셔너리
hex_to_bin = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}

# 암호코드 가로 길이비
ratio = {
    (2, 1, 1): 0, (2, 2, 1): 1, (1, 2, 2): 2, (4, 1, 1): 3,
    (1, 3, 2): 4, (2, 3, 1): 5, (1, 1, 4): 6, (3, 1, 2): 7,
    (2, 1, 3): 8, (1, 1, 2): 9
}

TC = int(input())
for tc in range(TC):
    N, M = map(int, input().split())

    grid = []
    for _ in range(N):
        grid.append(list(map(str, input().rstrip())))
    # print(grid)

    visited_codes = []  # 코드 저장하는 리스트
    total_sum = 0

    for row in grid:
        # 16진수를 2진수 문자열로 변환
        bin_num = ""
        for char in row:
            bin_num += hex_to_bin[char]

        # print(bin_num)
        i = len(bin_num) - 1

        nums = []

        while i >= 0:
            if bin_num[i] == '1':
                c3 = c2 = c1 = 0

                # 맨 뒤 1의 연속 개수 카운트
                while i >= 0 and bin_num[i] == '1':
                    c3 += 1
                    i -= 1
                # 그 앞 0의 연속 개수 카운트
                while i >= 0 and bin_num[i] == '0':
                    c2 += 1
                    i -= 1
                # 그 앞 1의 연속 개수 카운트
                while i >= 0 and bin_num[i] == '1':
                    c1 += 1
                    i -= 1

                # 배율 알아내기
                # 얘가 원래 비임
                min_c = min(c1, c2, c3)
                # 간단한 자연수의 비
                r1, r2, r3 = c1 // min_c, c2 // min_c, c3 // min_c
                # 비율을 넣음
                nums.append(ratio[(r1, r2, r3)])

                if len(nums) == 8:      # 숫자 8개를 모두 찾았다면
                    nums = nums[::-1]   # 뒤에서부터 찾았으므로 리스트를 뒤집어줌

                    # 같은 코드가 여러줄 있으니까 처음 발견한 암호코드 배열인지 확인
                    if nums not in visited_codes:
                        visited_codes.append(nums)  # 중복 방지를 위해 하나만 저장

                        odd_sum = nums[0] + nums[2] + nums[4] + nums[6]
                        even_sum = nums[1] + nums[3] + nums[5]
                        verify_num = nums[7]

                        if ((odd_sum * 3) + even_sum + verify_num) % 10 == 0:
                            total_sum += sum(nums)

                    nums = []  # 같은 줄에 코드 더 있을 수 있으니 초기화
            else:
                i -= 1  # 못찾았으면 왼쪽으로 이동

    print(f"#{tc+1} {total_sum}")