def merge_sort(arr):
    global count
    # 1. 분할
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # 2. 문제 조건 체크 (병합 전 왼쪽 끝과 오른쪽 끝 비교)
    if left[-1] > right[-1]:
        count += 1

    # 3. 병합
    return merge(left, right)

def merge(left, right):
    result = []
    left_idx = right_idx = 0
    
    # 두 리스트의 요소를 비교하며 작은 순서대로 결과에 담기
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    
    # 남은 요소들 붙이기
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    
    return result


TC = int(input())
for tc in range(TC):
    N = int(input())
    data = list(map(int, input().split()))
    
    count = 0
    sorted_data = merge_sort(data)
    
    print(f"#{tc+1} {sorted_data[N // 2]} {count}")