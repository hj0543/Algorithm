import sys
input = sys.stdin.readline

N = int(input())
heights = [0] * N
for i in range(N):
    heights[i] = int(input())
# print(heights)

heights.append(0)
stack = []
max_area = 0

for i in range(N + 1):
    while stack and heights[stack[-1]] > heights[i]:
        h = heights[stack.pop()]
        if not stack:
            w = i
        else:
            w = i - stack[-1] - 1

        max_area = max(max_area, h * w)

    stack.append(i)

print(max_area)