import sys
sys.stdin = open('input.txt', 'r')

##################################################
# 16진수를 10진수로
def hex_to_int(tar, base):
    total_sum = 0

    reversed_list = list(tar)
    reversed_list.reverse()

    hex_map = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    for i in range(len(reversed_list)):
        char = reversed_list[i]

        if base == 16 and char in hex_map:
            val = hex_map[char]
        else:
            val = int(char)

        total_sum += val * (base ** i)

    return total_sum

# 10진수를 2진수로
def int_to_bi(tar):
    result = []

    while tar != 0:
        result.append(tar % 2)
        tar //= 2

    result.reverse()

    while len(result) < 4:
        result.insert(0, 0)

    return result

decode_number = {
    "001101": 0, "010011": 1, "111011": 2, "110001": 3,
    "100011": 4, "110111": 5, "001011": 6, "111101": 7,
    "011001": 8, "101111": 9
}

TC = int(input())
for tc in range(TC):
    number_data = input()
    # print(number_data)

    int_num = []
    for i in range(len(number_data)):
        int_num.append(hex_to_int(number_data[i], 16))
    # print(int_num)

    bi_num = ""
    for i in range(len(int_num)):
        bi_num += "".join(map(str, int_to_bi(int_num[i])))
    # print(bi_num)

    result = []
    found = False
    for i in range(len(bi_num) - 5):
        code = bi_num[i: i + 6]

        if code in decode_number:
            for j in range(i, len(bi_num)-i, 6):
                number = bi_num[j:j+6]
                result.append(number)
            found = True
        if found:
            break
    # print(result)

    print(f"#{tc + 1}", end=' ')
    for i in range(len(result)):
        print(decode_number[result[i]], end=' ')
    print()