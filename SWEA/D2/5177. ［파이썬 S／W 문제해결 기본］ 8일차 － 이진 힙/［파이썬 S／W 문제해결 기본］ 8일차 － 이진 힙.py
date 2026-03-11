# [로직전략]
# 최소 힙 삽입 함수 (push)
# 1. 삽입 : 배열의 가장 마지막에 새로운 값을 추가
# 2. 힙 조건 유지(Up-Heap) : 부모 노드(curr // 2)의 값이 현재 노드(curr)의 값보다 크면 두 값을 교환 (루트에 도달하거나 부모가 더 작아질 때까지 반복)

def push(value):
    # 1. 삽입
    heap.append(value)
    curr = len(heap) - 1
    
    # 2. 힙 조건 유지 (부모 노드와 비교 및 교환)
    while curr > 1 and heap[curr] < heap[curr // 2]:
        heap[curr], heap[curr // 2] = heap[curr // 2], heap[curr]
        curr //= 2

TC = int(input())
for tc in range(TC):
    N = int(input())
    data = list(map(int, input().split()))
    
    heap = [0]
    for num in data:
        push(num)
        
    # 마지막 노드의 조상 노드 합 구하기
    ans = 0
    node = N // 2
    while node > 0:
        ans += heap[node]
        node //= 2
        
    print(f'#{tc+1} {ans}')