import sys

nums = list(map(int, sys.stdin.buffer.read().split()))

max_num = max(nums)

print(max_num, nums.index(max_num) + 1, sep = "\n")