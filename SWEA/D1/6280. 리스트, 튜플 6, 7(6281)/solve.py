import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

measure = []

for nums in range(1, N + 1):
    if N % nums == 0:
        measure.append(nums)

print(measure)