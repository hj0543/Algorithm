import heapq

TC = int(input())
for tc in range(TC):
    n = int(input())
    arr = list(map(int, input().split()))
    
    pq = []
    
    for i in arr:
        heapq.heappush(pq, i)

    pq = [0] + pq
    # 3. 마지막 노드(n)의 부모 노드들 합 구하기
    result = 0
    p = n // 2
    while p >= 1:
        result += pq[p]
        p //= 2
        
    print(f'#{tc+1} {result}')