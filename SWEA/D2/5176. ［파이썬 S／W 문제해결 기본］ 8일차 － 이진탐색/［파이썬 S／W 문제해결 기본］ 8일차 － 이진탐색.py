# [로직전략]
# 중위 순회 함수 (in_order)
# 1. 종료조건 : 현재 노드 번호가 N을 초과하면 return (존재하지 않는 노드)
# 2. 왼쪽 자식 탐색 : 현재 노드(node) * 2 로 이동
# 3. 노드 값 할당 : 현재 노드에 1부터 차례대로 증가하는 값을 저장
# 4. 오른쪽 자식 탐색 : 현재 노드(node) * 2 + 1 로 이동

def in_order(node):
    global number
    
    # 1. 종료조건
    if node > N:
        return
        
    # 2. 왼쪽 자식 탐색
    in_order(node * 2)
    
    # 3. 노드 값 할당
    tree[node] = number
    number += 1
    
    # 4. 오른쪽 자식 탐색
    in_order(node * 2 + 1)

TC = int(input())
for tc in range(TC):
    N = int(input())
    tree = [0] * (N + 1)
    number = 1
    
    in_order(1)
    
    print(f'#{tc+1} {tree[1]} {tree[N//2]}')