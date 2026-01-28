N = int(input())

nums = list(map(int, input().split()))
sort_nums = sorted(nums)

n = len(sort_nums)

if len(nums) % 2 == 0:
    result = sort_nums[0] * sort_nums[-1] # 약수의 개수가 짝수이면 진짜 약수 중 최솟값과 최댓값을 곱한다.
else:
    result = sort_nums[n // 2] ** 2 # 약수의 개수가 홀수이면 진짜 약수의 중앙값을 제곱한다.

print(result)