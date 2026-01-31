import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

new_nums = sorted(nums) # 오름차순 정렬


total = 0

# 무조건 작은놈을 젤 앞으로 보내야 한다.
# 그러므로 N명이 있다면 첫 번째는 N을 곱한 수 만큼 더하고
# 두 번째는 N-1만큼 곱하면 되니까 
for i in range(N):
    total += new_nums[i] * (N - i)


print(total)