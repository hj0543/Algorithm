import sys
sys.stdin = open('input.txt', 'r')

N = input()

nums = list(map(int, N))

print(sum(nums))