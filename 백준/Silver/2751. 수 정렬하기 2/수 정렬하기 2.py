import sys
N = int(sys.stdin.readline())


numbers = [] # sort쓸거니까 빈 리스트에 저장하고


for _ in range(N):
    numbers.append(int(sys.stdin.readline()))

sort_nums = sorted(numbers) # sorted 사용해서 오름차순 정렬


for j in range(len(sort_nums)):
    print(sort_nums[j])
