import sys
sys.stdin = open('input.txt', 'r')

nums = [int(input()) for i in range(5)]
# nums = []

# for i in range(5):
#     nums.append(int(input()))

print(f'입력된 값 {nums}의 평균은 {sum(nums)/5}입니다.')