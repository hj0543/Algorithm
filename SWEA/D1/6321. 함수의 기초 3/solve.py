import sys
sys.stdin = open('input.txt', 'r')

num = int(input())

nums = []

for n in range(1, num + 1):
    if num % n == 0:
        nums.append(n)


def prime_num(a):
    len(a) == 2
    return '소수입니다.'

print(prime_num(nums))



