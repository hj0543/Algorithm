import sys

checked_nums = list(map(int, sys.stdin.buffer.read().split()))

nums = list(range(1, 31)) #(1, 30)하면 틀림

absence_nums = sorted(set(nums) - set(checked_nums))

for x in absence_nums:
    print(x)