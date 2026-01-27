import sys
sys.stdin = open('input.txt', 'r')

nums = list(map(int, input().split()))

total = 0

for i in range(len(nums)):
    total += (nums[i] ** 2)

print(total % 10)