import sys
input = sys.stdin.readline

def lower_bound(arr, target):
    start, end = 0, len(arr)
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid
    return start

def upper_bound(arr, target):
    start, end = 0, len(arr)
    while start < end:
        mid = (start + end) // 2
        if arr[mid] <= target:
            start = mid + 1
        else:
            end = mid
    return start

N = int(input())
finder = list(map(int, input().split()))
find_range = sorted(finder)

M = int(input())
target = list(map(int, input().split()))
result = [0] * M

for i in range(M):
    result[i] += upper_bound(find_range, target[i]) - lower_bound(find_range, target[i])

print(*result)