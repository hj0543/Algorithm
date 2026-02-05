import sys
sys.stdin = open('input.txt', 'r')

# 7568
import sys
input = sys.stdin.readline


TC = int(input())

weight = []
height = []
nums = [i for i in range(TC)]
rank = []

for i in range(TC):
    w, h = map(int, input().split())
    weight.append(w)
    height.append(h)

for i in range(len(weight)):
    for j in range(len(weight) - 1):
        if weight[j] < weight[j + 1]:
            weight[j], weight[j + 1] = weight[j + 1], weight[j]
            height[j], height[j + 1] = height[j + 1], height[j]
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

for i in range(len(TC)-1):
    if nums[i] > nums[i+1]:
        rank.append(nums[i+1])