# BOJ 2042. 구간 합 구하기
# 세그먼트 트리
import sys
input = sys.stdin.readline


# 1. 트리 초기화 함수
def init(node, start, end):
    # 리프 노드인 경우 (구간의 시작과 끝이 같은 경우) 원본 배열의 값을 트리에 저장
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    
    mid = (start + end) // 2
    # 왼쪽 자식과 오른쪽 자식 트리를 재귀적으로 초기화하고, 두 값의 합을 부모 노드에 저장
    tree[node] = init(node * 2, start, mid) + init(node * 2 + 1, mid + 1, end)
    return tree[node]


# 2. 데이터 변경 함수
# index: 변경할 원본 배열 인덱스, diff: 변경된 차이값
def update(node, start, end, index, diff):
    # 변경할 인덱스가 현재 노드의 담당 구간에 포함되지 않으면 무시
    if index < start or index > end:
        return
    
    # 구간에 포함된다면 현재 노드의 값 갱신
    if index >= start and index <= end:
        tree[node] += diff
    
    # 리프 노드가 아니라면 자식 노드들도 재귀적으로 갱신
    if start != end:
        mid = (start + end) // 2
        update(node * 2, start, mid, index, diff)
        update(node * 2 + 1, mid + 1, end, index, diff)

    return tree[node]


# 3. 구간 합 구하기 함수
# left, right: 구간의 시작과 끝
def query(node, start, end, left, right):
    # 1) 목표 구간이 현재 노드의 구간과 전혀 겹치지 않는 경우
    if left > end or right < start:
        return 0
    
    # 2) 목표 구간이 현재 노드의 구간을 완전히 포함하는 경우
    if left <= start and end <= right:
        return tree[node]
    
    # 3) 구간이 일부만 겹치는 경우, 자식 노드들로 내려가서 탐색 후 합산
    mid = (start + end) // 2
    return query(node * 2, start, mid, left, right) + query(node * 2 + 1, mid + 1, end, left, right)


# -----------------------------------------------------------------------------------------------

# 입력부

# N: 수의 개수 / M: 수의 변경이 일어나는 횟수 / K: 구간의 합을 구하는 횟수
N, M, K = map(int, input().split())

# N개의 수
arr = [int(input()) for _ in range(N)]

tree = [0] * (N * 4)

# 트리 초기화
init(1, 0, N-1)

for _ in range(M + K):
    a, b, c = map(int, input().split())
    # a가 1인경우 b번째 수를 c로 바꾸고,    
    if a == 1:
       b -= 1
       diff = c - arr[b]
       arr[b] = c
       update(1, 0, N-1, b, diff)         

    # a가 2인 경우에는 b번째 수부터 c번째 수까지의 합을 구하여 출력
    elif a == 2:
        print(query(1, 0, N-1, b-1, c-1))


