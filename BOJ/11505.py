import sys
input = sys.stdin.readline

num = 1000000007


# 1. 트리 초기화 함수
def init(node, start, end):
    # 리프 노드인 경우 원본 배열의 값을 트리에 저장
    if start == end:
        tree[node] = arr[start]
        return tree[node]

    # 왼쪽 자식과 오른쪽 자식을 초기화한 뒤 두 값의 곱을 현재 노드에 저장
    mid = (start + end) // 2
    left_value = init(node * 2, start, mid)
    right_value = init(node * 2 + 1, mid + 1, end)
    tree[node] = (left_value * right_value) % num
    return tree[node]


# 2. 데이터 변경 함수
# index: 변경할 원본 배열 인덱스 / value: 새 값
def update(node, start, end, index, value):
    # 변경할 인덱스가 현재 노드 구간에 포함되지 않으면 현재 값을 그대로 반환
    if index < start or index > end:
        return tree[node]

    # 리프 노드라면 해당 위치를 새 값으로 갱신
    if start == end:
        tree[node] = value
        return tree[node]

    # 자식 노드를 갱신한 뒤 두 값의 곱으로 현재 노드를 다시 계산
    mid = (start + end) // 2
    left_value = update(node * 2, start, mid, index, value)
    right_value = update(node * 2 + 1, mid + 1, end, index, value)
    tree[node] = (left_value * right_value) % num
    return tree[node]


# 3. 구간 곱 구하기 함수
# left, right: 구간의 시작과 끝
def query(node, start, end, left, right):
    # 1) 목표 구간과 현재 노드 구간이 전혀 겹치지 않는 경우
    if left > end or right < start:
        return 1

    # 2) 목표 구간이 현재 노드 구간을 완전히 포함하는 경우
    if left <= start and end <= right:
        return tree[node]

    # 3) 구간이 일부만 겹치는 경우, 자식 노드로 내려가 곱을 계산
    mid = (start + end) // 2
    left_value = query(node * 2, start, mid, left, right)
    right_value = query(node * 2 + 1, mid + 1, end, left, right)

    return (left_value * right_value) % num


# -----------------------------------------------------------------------------------------------

# 입력부

# N: 수의 개수 / M: 변경이 일어나는 횟수 / K: 구간 곱을 구하는 횟수
N, M, K = map(int, input().split())

# N개의 수
arr = [int(input()) for _ in range(N)]

tree = [0] * (N * 4)

# 트리 초기화
init(1, 0, N - 1)

for _ in range(M + K):
    a, b, c = map(int, input().split())

    # a가 1이면 b번째 수를 c로 변경
    if a == 1:
        arr[b - 1] = c
        update(1, 0, N - 1, b - 1, c)

    # a가 2이면 b번째 수부터 c번째 수까지의 곱을 출력
    elif a == 2:
        print(query(1, 0, N - 1, b - 1, c - 1))
