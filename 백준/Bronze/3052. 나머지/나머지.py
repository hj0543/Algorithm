import sys

nums = list(map(int, sys.stdin.buffer.read().split()))

result = []

for i in nums:
  result.append(i % 42)

setting = set(result)

print(len(setting))