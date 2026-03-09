
A = [i for i in range(1, 13)]
n_A = len(A)

TC = int(input())

for tc in range(TC):
    N, K = map(int, input().split())
    result = 0

    # 모든 부분집합 생성
    for i in range(1 << n_A):
        subset_sum = 0
        subset_count = 0
        
        # 각 비트를 확인하여 부분집합 구성
        for j in range(n_A):
            if i & (1 << j): # i의 j번째 비트가 1이면 A[j] 포함
                subset_sum += A[j]
                subset_count += 1
        
        # 원소 개수가 N이고 합이 K?
        if subset_count == N and subset_sum == K:
            result += 1

    print(f"#{tc+1} {result}")