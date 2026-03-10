def quick_sort(arr, left, right):
    if left < right:
        # 파티션 과정을 거쳐 피벗의 위치를 결정
        p = partition(arr, left, right)
        # 피벗을 기준으로 좌우 재귀 호출
        quick_sort(arr, left, p - 1)
        quick_sort(arr, p + 1, right)

def partition(arr, left, right):
    pivot = arr[left]  # 가장 왼쪽 원소를 피벗으로 설정
    i, j = left, right
    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[left], arr[j] = arr[j], arr[left] # 피벗을 제자리로 이동
    return j

TC = int(input())
for tc in range(TC):
    N = int(input())
    data = list(map(int, input().split()))
    
    quick_sort(data, 0, N - 1)
    
    print(f"#{tc+1} {data[N // 2]}")