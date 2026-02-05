num = int(input())

nums = []

for n in range(1, num + 1):
    if num % n == 0:
        nums.append(n)


def prime_num(nums):
    len(nums) == 2
    return '소수입니다.'

print(prime_num(nums))