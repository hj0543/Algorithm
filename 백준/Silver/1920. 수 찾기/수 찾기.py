import sys
input = sys.stdin.readline

def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    # start가 end를 넘어설 때까지 반복
    while start <= end:
        mid = (start + end) // 2

        # 값을 찾은 경우
        if arr[mid] == target:
            return 1

            # target이 중간값보다 큰 경우 (오른쪽 확인)
        elif arr[mid] < target:
            start = mid + 1

        # target이 중간값보다 작은 경우 (왼쪽 확인)
        else:
            end = mid - 1

    return 0  # 찾는 값이 없을 때

N = int(input())
finder = list(map(int, input().split()))
find_range = sorted(finder)

M = int(input())
target = list(map(int, input().split()))

for i in range(M):
    print(binary_search(find_range, target[i]))