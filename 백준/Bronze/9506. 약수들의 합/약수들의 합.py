import sys
input = sys.stdin.readline

def div(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

#############################################################################

while True:
    n = input().strip() # 한 줄 읽고 양옆 공백 제거
    number = int(n)
    if number == -1:
        break

    slice_numbers = div(number)

    total = sum(slice_numbers[:-1])
    '''
    print(total)
    6
    16
    28
    '''
    str1 = div(number)[:-1]
    plus = ' + '.join(map(str, str1))

    if total == number:
        print(f'{number} = {plus}')
    else:
        print(f'{number} is NOT perfect.')