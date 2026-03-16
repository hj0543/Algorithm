import sys
input = sys.stdin.readline

# 제목은 버블소트인데 병합정렬로 풀어야하는 이상한 문제;;

def merge_sort(start, end):

    if start >= end:
        return

    mid = (start + end) // 2
    
    merge_sort(start, mid)
    merge_sort(mid + 1, end)
    
    merge(start, mid, end)

def merge(start, mid, end):
    global swap_count
    
    i = start
    j = mid + 1
    temp = []
    
    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            swap_count += (mid - i + 1) # 도라이;;
            temp.append(arr[j])
            j += 1
            
    while i <= mid:
        temp.append(arr[i])
        i += 1
    while j <= end:
        temp.append(arr[j])
        j += 1
        
    for k in range(len(temp)):
        arr[start + k] = temp[k]


N = int(input())
arr = list(map(int, input().split()))
swap_count = 0

merge_sort(0, N - 1)

# 결과 출력
print(swap_count)