def binary_search(arr, target, N):
    low = 0
    high = N - 1
    last_dir = 0  # 0: 시작, 1: 왼쪽, 2: 오른쪽
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return True
        
        # 왼쪽으로 가야 하는 상황
        elif arr[mid] > target:           
            if last_dir == 1: # 이미 직전에 왼쪽이었으면 실패
                return False
            high = mid - 1
            last_dir = 1
            
        # 오른쪽으로 가야 하는 상황    
        else:        
            if last_dir == 2: # 이미 직전에 오른쪽이었으면 실패
                return False
            low = mid + 1
            last_dir = 2
            
    return False

TC = int(input())
for tc in range(TC):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split()))) # A는 반드시 정렬
    B = list(map(int, input().split()))
    
    result = 0
    for target in B:
        if binary_search(A, target, N):
            result += 1
            
    print(f"#{tc+1} {result}")