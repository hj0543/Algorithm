import sys
sys.stdin = open('input.txt', 'r')

# 42476
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

if n == 1:
    print(1)
    sys.exit()


cnt1 = []
cnt2 = []
total = 0



for i in range(1, n):
    if nums[i] <= nums[i - 1]:
        total += 1
    else:
        cnt1.append(total)
        total = 0
cnt1.append(total)

total = 0

for i in range(1, n):
    if nums[i] >= nums[i - 1]:
        total += 1
    else:
        cnt2.append(total)
        total = 0
cnt2.append(total)    

result1 = max(cnt1)
result2 = max(cnt2)


if result1 >= result2:
    print(result1 + 1)

else:
    print(result2 + 1)


