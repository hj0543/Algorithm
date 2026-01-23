import sys
sys.stdin = open('input.txt', 'r')

nums = list(map(int, sys.stdin.buffer.read().split()))

for i in nums:
  i %= 42

print(i)
