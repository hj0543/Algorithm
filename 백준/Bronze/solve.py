import sys
sys.stdin = open('input.txt', 'r')

import sys

nums = list(map(int, sys.stdin.buffer.read().split()))

max_num = max(nums)

print(max_num, nums.index(max_num) + 1, sep = "\n")
# print(max_num)
# print(sorted_nums.index(max_num))